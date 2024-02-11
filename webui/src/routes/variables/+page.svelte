<script>
	import { goto, preloadData } from '$app/navigation';
	import { Input } from '$lib/components/ui/input';
	import { debounce } from 'lodash-es';
	import { Table, TableRow, TableHead, TableHeader, TableCell } from '$lib/components/ui/table';

	export let data;

	let handleSearch = debounce((e) => {
		let search_term = e.target.value;

		const url = `/api/variables/search/${search_term}`;
		fetch(url)
			.then((res) => res.json())
			.then((res) => {
				data.variables = res;
			});
	}, 300);
</script>

<h1 class="text-2xl">Variables</h1>

<form>
	<Input on:input={handleSearch} type="text" placeholder="Search..." name="term" />
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
		<TableRow class="hover:cursor-pointer" on:click={goto(`/variables/${variable.id}`)} on:mouseover={preloadData(`/variables/${variable.id}`)}>
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
