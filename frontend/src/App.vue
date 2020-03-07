<template>
  <div id="app">
    <router-view/>
    <footer class="footer">
      <div class="columns">
        <div class="column">
          <div class="content has-text-centered patreon">
            Become a
            <a href="https://www.patreon.com/retardedota">
                <img src="./assets/Patreon_White.png" class="img">
            </a>
            to
            <a class="pat-link" href="https://www.patreon.com/retardedota">support</a>
            Retarded Dota.
          </div>
        </div>
        <div class="column">
          <div class="content has-text-centered git">
            This is an open source project available on <a href="https://github.com/radostkali/retardedota" class="link">github</a>.
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

.patreon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.pat-link {
  margin: 0 0.4rem;
}

.img {
  display: inline-block;
  padding-top: 0.6rem;
  height: 71px;
  margin: 0 0.5rem;
}

.git {
  margin-top: 1.7rem;
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
$card-background-color: #161616;
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
