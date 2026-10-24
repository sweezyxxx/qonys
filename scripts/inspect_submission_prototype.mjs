import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const base = path.resolve('docs/submission-2026-10-24/prototype');
const out = path.join(base, 'screens');
await fs.mkdir(out, { recursive: true });
const reportOut = path.join(base, 'report-screens');
await fs.mkdir(reportOut, { recursive: true });
const browser = await chromium.launch({ headless: true, ...(process.env.CHROMIUM_PATH ? {executablePath: process.env.CHROMIUM_PATH} : {}) });
const page = await browser.newPage({ viewport: { width: 1280, height: 1050 }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', e => errors.push(e.message));
const check = (value, message) => { if (!value) throw new Error(message); };
const go = view => page.locator(`.routes button[data-go="${view}"]`).click();
const captureScreens = process.argv.includes('--screenshots');
const shot = async name => {
  if (!captureScreens) return;
  await page.screenshot({ path: path.join(out, name + '.png'), fullPage: true });
  await page.locator('main').screenshot({ path: path.join(reportOut, name + '.png') });
};
try {
  await page.goto(pathToFileURL(path.join(base, 'index.html')).href);
  await shot('01-catalogue');
  await page.locator('[data-project="court"]').click();
  await shot('02-development');
  await page.getByRole('button', { name: 'View floor 5', exact: true }).click();
  await shot('03-floor');
  await page.getByRole('button', { name: 'View apartment', exact: true }).click();
  await page.locator('#finishing').selectOption('whitebox');
  check((await page.locator('.price').innerText()).includes('32,400,000'), 'Selected finishing price did not update');
  await shot('04-apartment');
  await page.locator('#add-compare').click();
  await go('enquiry');
  check(await page.getByRole('heading', { name: 'Sign in to send an enquiry' }).isVisible(), 'Guest enquiry was not gated');
  await page.locator('#signin-enquiry').click();
  await page.locator('#login-form button[type="submit"]').click();
  check(await page.locator('#enquiry-form').isVisible(), 'Verified fixture did not reach enquiry form');
  check((await page.locator('#compare-count').innerText()) === '1', 'Comparison was lost on sign-in');
  await shot('05-enquiry');
  await page.locator('#enquiry-form button[type="submit"]').click();
  check((await page.locator('main').innerText()).includes('WhiteBox'), 'Submitted finishing was lost');
  await go('developer');
  await page.locator('#region-right').click();
  await page.locator('#review-region').click();
  check((await page.locator('#region-result').innerText()).includes('reviewed'), 'Region review did not update');
  await shot('06-developer-regions');
  await page.locator('[data-dev="Preview and publication"]').click();
  check(await page.locator('#publish').isDisabled(), 'Missing translation did not block publication');
  await shot('07-publication');
  await page.locator('#draft-description').fill('A fictional development description for the design review.');
  await page.locator('#save-draft').click();
  await page.locator('#publish').click();
  check((await page.locator('main').innerText()).includes('Published'), 'Publication fixture did not update');
  await page.locator('[data-dev="Enquiries"]').click();
  check((await page.locator('main').innerText()).includes('32,400,000'), 'Inbox did not preserve submitted price');
  await page.locator('#enquiry-status').selectOption('In progress');
  await shot('08-developer-enquiries');
  await go('admin');
  await page.locator('#moderate').click();
  check((await page.locator('#moderation-error').innerText()).includes('Enter a reason'), 'Missing reason was accepted');
  await page.locator('#hide-reason').fill('Incorrect development description; correction requested.');
  await page.locator('#moderate').click();
  await shot('09-administrator');
  await go('catalogue');
  check(!(await page.locator('main').innerText()).includes('Demo Court'), 'Hidden development remained in catalogue');
  await go('development');
  check(await page.getByRole('heading', { name: 'Development unavailable' }).isVisible(), 'Hidden direct content remained visible');
  await go('developer');
  await page.locator('[data-dev="My developments"]').click();
  check((await page.locator('main').innerText()).includes('Incorrect development description'), 'Owner cannot see hiding reason');
  await go('admin');
  await page.locator('#company-access').click();
  await page.locator('#company-access').click();
  check(await page.getByText('Sample Developer · Hidden', { exact: true }).isVisible(), 'Company reactivation removed individual restriction');
  await page.locator('#moderate').click();
  await go('catalogue');
  check(await page.getByRole('heading', { name: 'Demo Court', exact: true }).isVisible(), 'Development was not restored');
  for (const width of [320, 736, 1024]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const view of ['catalogue', 'development', 'floor', 'apartment', 'enquiry', 'developer', 'admin']) {
      await go(view);
      const size = await page.evaluate(() => ({ scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth }));
      check(size.scroll <= size.client + 1, `Horizontal overflow at ${width}px on ${view}`);
    }
  }
  check(errors.length === 0, 'Browser script errors: ' + errors.join('; '));
  const recordDir = captureScreens ? base : path.resolve('work/verification');
  await fs.mkdir(recordDir, {recursive: true});
  await fs.writeFile(path.join(recordDir, 'prototype-inspection.json'), JSON.stringify({ scope: 'Local HTML design prototype only', inspectedAt: new Date().toISOString(), screenshotCount: captureScreens ? 9 : 0, widths: [320,736,1024], checks: ['finishing selection', 'guest enquiry gate', 'comparison retained on sign-in', 'enquiry context', 'region correction/review', 'publication blocker and completion', 'inbox status', 'moderation reason', 'hidden catalogue/direct content', 'company restoration preserves restriction', 'development restoration', 'responsive width'], browserErrors: errors, outcome: 'Passed' }, null, 2));
  console.log('Prototype interaction inspection passed. Screenshot capture: ' + (captureScreens ? 'enabled' : 'disabled') + '.');
} finally {
  await browser.close();
}
