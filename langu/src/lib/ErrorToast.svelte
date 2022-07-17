<script>
    export let hidden = true;
</script>

<div
    id="error-toast"
    class="toast toast-center toast-middle"
    class:hidden
    title="Click to hide"
    on:click={() => {
        hidden = true;
    }}
>
    <div class="alert alert-error">
        <div>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current flex-shrink-0 h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
            </svg>
            <span class="short-error-description"><slot /></span>
        </div>
        <slot name="long-description" />
    </div>
</div>

<style>
    #error-toast {
        z-index: 9001;
    }
    .alert {
        min-width: 35ch;
        max-width: 60ch;
        flex-direction: column;
    }
    .short-error-description {
        font-weight: 550;
    }
</style>
