<script>
    export let buttonLabel = "Click me";
    export let onClick;
</script>

<div class="dropdown-outer">
    <slot name="button">
        <button class="dropdown-btn" on:click={onClick}>
            {buttonLabel}
        </button>
    </slot>
    <div class="dropdown-menu">
        <button class="dropdown-handle">▾</button>
        <div class="dropdown-items">
            <slot />
        </div>
    </div>
</div>

<style>
    .dropdown-outer {
        display: inline-flex;
        border-radius: 0.4rem;
        overflow: hidden;
        outline: 1px solid transparent;
        transition: outline-color 0.2s;
    }
    .dropdown-outer > :global(.dropdown-btn) {
        background-color: var(--button-bg-color);
        padding: 0.5em 0.8em 0.5em 1em;
        cursor: pointer;
        border: none;
        border-right: 2px solid rgba(0, 0, 0, 0.2);
        font-size: 1em;
        font-weight: 500;
        font-family: inherit;
    }
    .dropdown-menu {
        border-radius: 8px;
    }
    .dropdown-items {
        position: absolute;
        max-height: 20em;
        overflow: scroll;
        display: none;
    }

    .dropdown-outer:hover {
        outline-color: #646cff;
    }
    .dropdown-menu:hover > .dropdown-items {
        display: block;
    }
    .dropdown-handle {
        background-color: var(--button-bg-color);
        padding: 0.5em 0.6em 0.5em 0.6em;
        cursor: pointer;
        border: 1px solid transparent;
        font-size: 1em;
        font-weight: 500;
        font-family: inherit;
    }
</style>
