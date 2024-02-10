<script>
    import { Table, TableRow, TableHead, TableHeader, TableCell } from '$lib/components/ui/table';
    import { goto } from '$app/navigation';
    export let data;
</script>


<h1 class="text-2xl">Details of {data.variable.description}</h1>

<section class="my-3">
    <ol class="list-disc list-inside">
        <li>Codebook: {data.variable.codebook.title}</li>
        <li>Variable name: {data.variable.name}</li>
        <li>Variable description: {data.variable.description}</li>
        <li>Values: {data.variable.values}</li>
        <li>Similar variables: {data.similar.length}</li>
    </ol>
</section>


<p>{data.variable.values}</p>

<h2 class="text-xl">Similar variables</h2>

<Table>
	<TableHeader>
		<TableRow>
			<TableHead>Codebook</TableHead>
			<TableHead>Date</TableHead>
			<TableHead>Name</TableHead>
			<TableHead>Description</TableHead>
			<TableHead>Values</TableHead>
		</TableRow>
	</TableHeader>

	{#each data.similar as variable}
		<TableRow class="hover:cursor-pointer" on:click={goto(`/variables/${variable.id}`)}>
			<TableCell>{variable.codebook.title}</TableCell>
			<TableCell>{variable.codebook.date}</TableCell>
			<TableCell><span class="bg-secondary rounded-sm p-1.5 font-mono">{variable.name}</span></TableCell>
			<TableCell>{variable.description}</TableCell>
			<TableCell><span class="whitespace-pre-line">{variable.values}</span></TableCell>
		</TableRow>
	{/each}
</Table>
