<script>
  import DarkModeToggle from "./lib/DarkModeToggle.svelte";
  import GithubLink from "./lib/GithubLink.svelte";
  import LearnSentence from "./lib/LearnSentence.svelte";

  const prefersLightMode =
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: light)").matches;
  let darkMode = !prefersLightMode;

  $: {
    if (darkMode) {
      document.body.setAttribute("data-theme", "dark");
    } else {
      document.body.setAttribute("data-theme", "light");
    }
  }
</script>

<main>
  <div class="navbar p-0">
    <div class="flex-1">
      <h1 id="page-title" class="flex-1">Langu</h1>
    </div>
    <ul id="link-menu" class="flex-none menu menu-horizontal">
      <li id="gh-link">
        <GithubLink class="w-8 h-8" repo="andriamanitra/langu" />
      </li>
      <li id="dark-mode-btn">
        <DarkModeToggle class="w-8 h-8" bind:darkModeEnabled={darkMode} />
      </li>
    </ul>
  </div>
  <div class="divider" />
  <LearnSentence />
</main>

<style>
  main {
    margin: 0 auto;
    width: min(100vw, 60rem);
  }
  .divider {
    margin-top: 0;
  }
</style>
