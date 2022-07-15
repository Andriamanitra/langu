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

<h2>Original sentence</h2>
<a class="tatoeba-link" href="https://tatoeba.org/en/sentences/show/{ru_id}">
  View on Tatoeba
</a>
<div class="original sentence">{ru}</div>

<Listen bind:whatToSay={ru} lang="ru" />

<button on:click={getRandom}> Another </button>

<h2>Translations</h2>

{#each en as translation}
  <div class="sentence translation">{translation}</div>
{/each}

<style>
  .sentence {
    padding: 0.2em;
    margin: 0.5em;
  }
  h2 {
    margin-bottom: 0px;
  }
  .tatoeba-link {
    font-size: 0.85em;
    text-decoration: underline;
  }
  .original {
    font-size: 1.3em;
  }

  button {
    border-radius: 8px;
    border: 1px solid transparent;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    background-color: var(--button-bg-color);
    cursor: pointer;
    outline: 1px solid transparent;
    transition: outline-color 0.2s;
    margin-left: 2ch;
  }
  button:hover {
    outline-color: #646cff;
  }
</style>
