<script>
	import { goto, preloadData } from '$app/navigation';
	import { Input } from '$lib/components/ui/input';
	import { Select, SelectTrigger, SelectContent, SelectItem, SelectInput, SelectValue } from '$lib/components/ui/select';
	import { debounce } from 'lodash-es';
	import { Table, TableRow, TableHead, TableHeader, TableCell } from '$lib/components/ui/table';
	import { Button } from '$lib/components/ui/button';

	export let data;

	let search_term = '';
	let limit = 10;
	let offset = 0;

	let loadData = async (term = '', limit, offset) => {
		const url = `/api/variables/search/${term}?offset=${offset}&limit=${limit}`;
		return fetch(url).then((res) => res.json());
	}

	let handleSearch = debounce((e) => {
		search_term = e.target.value;

		// Reset offset
		let limit = 10;
		let offset = 0;

		loadData(search_term, limit, offset).then((res) => {
			data.variables = res;
			offset += parseInt(limit);
		});
	}, 300);

	let handleLoadMore = () => {
		loadData(search_term, limit, offset).then((res) => {
			data.variables = data.variables.concat(res);
			offset += parseInt(limit);
		});
	};
</script>

<h1 class="my-3 text-2xl">Variables</h1>

<form class="my-3">
	<div class="flex">
		<Input on:input={handleSearch} type="text" placeholder="Find variables... (Fuzzy semantic search supported)" name="term" />
		<Input class="ml-3 w-1/12" type="number" bind:value={limit}/>
	</div>
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

<div class="my-5 flex justify-center">
	<Button variant="outline" class="mx-auto" on:click={handleLoadMore}>Load more</Button>
</div>
