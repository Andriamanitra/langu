<script>
  import { onMount } from "svelte";
  import Listen from "./Listen.svelte";

  const MIN_QUEUE_LENGTH = 5;
  const getMoreSentences = async () => {
    fetch("http://localhost:5000/sentence/random?count=20")
      .then((resp) => resp.json())
      .then((data) => {
        queue.push(...data);
      });
  };
  const nextSentence = () => {
    if (queue.length > 0) {
      ({ ru, en, ru_id } = queue.shift());
    } else {
      console.warn("sentence queue is empty!");
    }
    if (queue.length < MIN_QUEUE_LENGTH) {
      getMoreSentences();
    }
  };
  let queue = [];
  let ru = "Язык открывает миры.";
  let en = ["Language opens worlds."];
  let ru_id = 6882113;
  onMount(getMoreSentences);
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
  <button class="btn btn-primary" on:click={nextSentence}> Another </button>
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
