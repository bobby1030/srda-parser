<script>
	import { goto, preloadData } from '$app/navigation';
	import { Input } from '$lib/components/ui/input';
	import { debounce } from 'lodash-es';
	import { Table, TableRow, TableHead, TableHeader, TableCell } from '$lib/components/ui/table';
	import { Button } from '$lib/components/ui/button';

	export let data;

	let limit = 10;
	let offset = 0;

	let handleSearch = debounce((e) => {
		let search_term = e.target.value;

		const url = `/api/variables/search/${search_term}?limit=${limit}`;
		fetch(url)
			.then((res) => res.json())
			.then((res) => {
				data.variables = res;
			});
	}, 300);

	let handleLoadMore = () => {
		offset += 10;
		const url = `/api/variables/?offset=${offset}`;
		fetch(url)
			.then((res) => res.json())
			.then((res) => {
				data.variables = data.variables.concat(res);
			});
	};
</script>

<h1 class="text-2xl my-3">Variables</h1>

<form class="my-3">
	<Input on:input={handleSearch} type="text" placeholder="Find variables..." name="term" />
</form>

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

	{#each data.variables as variable}
		<TableRow
			class="hover:cursor-pointer"
			on:click={goto(`/variables/${variable.id}`)}
			on:mouseover={preloadData(`/variables/${variable.id}`)}
		>
			<TableCell>{variable.codebook.title}</TableCell>
			<TableCell>{variable.codebook.date}</TableCell>
			<TableCell
				><span class="bg-secondary rounded-sm p-1.5 font-mono">{variable.name}</span></TableCell
			>
			<TableCell>{variable.description}</TableCell>
			<TableCell><span class="whitespace-pre-line">{variable.values}</span></TableCell>
		</TableRow>
	{/each}
</Table>

<div class="flex justify-center my-5">
	<Button variant="outline" class="mx-auto" on:click={handleLoadMore}>Load more</Button>
</div>
