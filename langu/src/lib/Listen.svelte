<script>
    import ButtonDropdown from "./ButtonDropdown.svelte";
    import DropdownItem from "./DropdownItem.svelte";

    const synth = window.speechSynthesis;
    const speak = () => {
        let utterance = new SpeechSynthesisUtterance(whatToSay);
        utterance.voice = voice;
        synth.speak(utterance);
    };
    export let lang;
    export let whatToSay;
    export let buttonLabel = "Listen";
    let voices = synth.getVoices().filter((v) => v.lang == lang);
    let voice;
</script>

<ButtonDropdown onClick={speak} {buttonLabel}>
    {#each voices as v, i}
        <DropdownItem
            onClick={() => {
                voice = voices[i];
                speak();
            }}
        >
            {v.name.split("+")[1]}
        </DropdownItem>
    {/each}
</ButtonDropdown>
