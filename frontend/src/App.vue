<template>
  <div id="app">
    <router-view/>
    <footer class="footer">
      <div class="columns">
        <div class="column">
          <div class="content has-text-centered">
            <a href="/">Home</a>
          </div>
        </div>
        <div class="column">
          <div class="content has-text-centered">
            This is an open source project available on <a href="http://github.com" class="link">github</a>.
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style lang="scss">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

accent {
  color: white !important;
}

html {
  background: #222222 !important;
}

// Import Bulma's core
@import "~bulma/sass/utilities/_all";

// Set your colors
$dark: #222222;
$dark-invert: findColorInvert($dark);

$primary: #D3151B;
$primary-invert: findColorInvert($primary);

$info: $white;
$info-invert: findColorInvert($info);

$light: #656565;
$light-invert: findColorInvert($light);

$footer-background-color: #353535;
$footer-color: $white;

$input-background-color: $dark;
$input-color: $white;

// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert)
);

// Card
$card-color: #afafaf;
$card-header-color: $white;
$card-background-color: rgb(22, 22, 22);
$card-footer-border-top: $light;

// Title
$title-color: $white;

// Progress bar
$progress-border-radius: 0.3rem;
$progress-bar-background-color: $light;
$progress-value-background-color: $primary;

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-hover: $white;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
