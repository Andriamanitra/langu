<script>
    export let lang;
    export let whatToSay;
    let voices;
    let voice = null;

    const synth = window.speechSynthesis;
    const speak = () => {
        let utterance = new SpeechSynthesisUtterance(whatToSay);
        utterance.lang = lang;
        if (voice !== null) {
            utterance.voice = voice;
        }
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

{#if voices.length > 1}
    <div class="dropdown dropdown-hover voice-picker">
        <button tabindex="0" class="btn btn-secondary dropdown-button"
            >{voice?.name ?? "Default"}</button
        >
        <ul tabindex="0" class="dropdown-content menu shadow bg-base-100">
            <li>
                <button class="pick-voice" on:click={() => pickVoice(null)}>
                    Default
                </button>
            </li>
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
{/if}
<button tabindex="0" class="listen btn btn-secondary" on:click={speak}>
    Listen
</button>

<style>
    .dropdown-hover:hover .dropdown-button {
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
    }
    .dropdown-button {
        box-shadow: none;
        white-space: nowrap;
        overflow: hidden;
        display: block;
        text-overflow: "";
    }
    .dropdown-content {
        overflow: auto;
        width: 100%;
        max-height: 35vh;
        border-bottom-left-radius: var(--rounded-btn, 0.5rem);
        border-bottom-right-radius: var(--rounded-btn, 0.5rem);
    }
    .voice-picker::before {
        content: "VOICE";
        position: absolute;
        width: 100%;
        text-align: center;
        line-height: 100%;
        top: 2px;
        left: 0px;
        font-size: 0.6em;
        font-weight: 800;
    }
</style>
