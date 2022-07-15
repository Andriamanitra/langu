<script>
    export let onClick;
</script>

<button class="dropdown-item" on:click={onClick}><slot /></button>

<style>
    .dropdown-item {
        display: block;
    }
    button {
        cursor: pointer;
        border: none;
        width: 100%;
        text-align: left;
        font-size: 0.9em;
        font-weight: 500;
        font-family: inherit;
    }
</style>
