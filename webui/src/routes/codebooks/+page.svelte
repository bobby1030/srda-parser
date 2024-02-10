<script>
    export let data;
</script>

<main>
    <h1 class="text-xl">Codebooks</h1>
    {#each data.codebooks as codebook}
        <p>{codebook.title}</p>
    {/each}
</main>