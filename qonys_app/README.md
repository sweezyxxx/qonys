# QONYS Flutter Web client

The client scaffold was introduced by Bexultan Nishanbek through [QON-2](https://qonys.youtrack.cloud/issue/QON-2), [commit 29e9e1b](https://github.com/sweezyxxx/qonys/commit/29e9e1b) and [PR 4](https://github.com/sweezyxxx/qonys/pull/4).

## Current contents

`lib/main.dart` contains the standard counter screen. `test/widget_test.dart` checks the counter increment. The `web/` directory contains the web runner; Android and iOS runner files are also present. The approved delivery target is Flutter Web. Catalogue screens, account flows and backend integration follow this initialization.

## Prerequisites

Install Flutter with a bundled Dart SDK satisfying `^3.13.5`, the constraint in `pubspec.yaml`. Run `flutter --version` to check the installed SDK. The recorded local environment has Flutter 3.44.2 and Dart 3.12.2, which cannot resolve this project; use a compatible SDK before running the commands below.

## Run

From `qonys_app/`:

```console
flutter pub get
flutter run -d chrome
```

## Check and build

After successful dependency resolution:

```console
flutter analyze
flutter test
flutter build web
```

The web output is written to `build/web/`. The [verification record](../docs/delivery/verification/frontend-scaffold.json) distinguishes the existing test source from executed checks. See the [project README](../README.md) for the scope, backend, documentation and contribution workflow.
