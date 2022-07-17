<script>
  import { onMount } from "svelte";
  import Listen from "./Listen.svelte";

  const getRandom = async () => {
    fetch("http://localhost:5000/sentence/random")
      .then((resp) => resp.json())
      .then((data) => {
        ru = data["ru"];
        en = data["en"];
        ru_id = data["ru_id"];
      });
  };
  let ru = "привет";
  let en = ["hello"];
  let ru_id = 0;
  onMount(getRandom);
</script>

<div class="original card">
  <div>
    <h2>Original sentence</h2>
  </div>
  <div>
    <a
      class="link link-accent"
      href="https://tatoeba.org/en/sentences/show/{ru_id}"
    >
      View on Tatoeba
    </a>
  </div>
  <div class="sentence">{ru}</div>
</div>

<div class="buttons">
  <Listen bind:whatToSay={ru} lang="ru" />
  <button class="btn btn-primary" on:click={getRandom}> Another </button>
</div>
<div class="translated card">
  <h2>Translations</h2>

  {#each en as translation}
    <div class="sentence">{translation}</div>
  {/each}
</div>

<style>
  .sentence {
    padding: 0.2em;
    margin: 0.5em;
  }
  .buttons {
    display: inline-flex;
    flex-wrap: wrap;
    justify-content: center;
    column-gap: 2em;
    row-gap: 1em;
  }
  .original .sentence {
    font-size: 1.3em;
  }
</style>
