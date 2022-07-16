<script>
    export let lang;
    export let whatToSay;
    let voices;
    let voice;

    const synth = window.speechSynthesis;
    const speak = () => {
        let utterance = new SpeechSynthesisUtterance(whatToSay);
        utterance.voice = voice;
        synth.speak(utterance);
    };
    const getVoices = () => {
        voices = synth.getVoices().filter((v) => v.lang == lang);
    };
    const pickVoice = (v) => {
        voice = v;
        speak();
    };
    getVoices();
    synth.addEventListener("voiceschanged", getVoices);
</script>

{#if voices.length > 0}
    <div class="dropdown dropdown-hover listen">
        <button tabindex="0" class="btn btn-secondary" on:click={speak}>
            Listen
        </button>
        <ul tabindex="0" class="dropdown-content menu shadow bg-base-100">
            {#each voices as voice}
                <li>
                    <button
                        class="pick-voice"
                        on:click={() => pickVoice(voice)}
                    >
                        {voice.name}
                    </button>
                </li>
            {/each}
        </ul>
    </div>
{:else}
    <button
        tabindex="0"
        class="btn btn-secondary"
        on:click={speak}
        title="Unable to detect SpeechSynthesisVoices, this button might not work"
    >
        Listen
    </button>
{/if}

<style>
    .dropdown-content {
        overflow: auto;
        max-height: 35vh;
    }
</style>
