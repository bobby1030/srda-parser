<script>
	import * as Table from '$lib/components/ui/table';
	import * as Card from '$lib/components/ui/card';
	import { goto } from '$app/navigation';
	export let data;
</script>

<h1 class="m-3 text-3xl">Variable Details</h1>

<Card.Root>
	<Card.Header>
		<Card.Description>
			<span class="inline-block"
				>{data.variable.codebook.title}（{data.variable.codebook.date}）</span
			>
			<span class="bg-secondary inline-block rounded-sm px-1.5 py-0.5 font-mono"
				>{data.variable.name}</span
			>
		</Card.Description>
		<Card.Title>{data.variable.description}</Card.Title>
	</Card.Header>
	<Card.Content>
		{#if data.variable.values}
			<section class="my-2">
				<h3 class="font-semibold">Values</h3>
				<p class="whitespace-pre-line">{data.variable.values}</p>
			</section>
		{/if}

		{#if data.variable.notes}
			<section class="my-2">
				<h3 class="font-semibold">Notes</h3>
				<p>{data.variable.notes}</p>
			</section>
		{/if}

		<section class="my-2">
			<h3 class="font-semibold">Similar variables in other codebooks: {data.similar_across_codebooks.length}</h3>
			<Table.Root>
				<Table.Header>
					<Table.Row>
						<Table.Head>Codebook</Table.Head>
						<Table.Head>Name</Table.Head>
						<Table.Head>Description</Table.Head>
						<Table.Head>Values</Table.Head>
					</Table.Row>
				</Table.Header>

				{#each data.similar_across_codebooks as variable}
					<Table.Row>
						<Table.Cell href={`/codebooks/${variable.codebook.id}`}
							>{variable.codebook.title}（{variable.codebook.date}）</Table.Cell
						>
						<Table.Cell href={`/variables/${variable.id}`}
							><span class="bg-secondary rounded-sm px-1.5 py-0.5 font-mono">{variable.name}</span
							></Table.Cell
						>
						<Table.Cell href={`/variables/${variable.id}`}>{variable.description}</Table.Cell>
						<Table.Cell
							><div class="max-h-16 overflow-y-scroll whitespace-pre-line">
								{variable.values}
							</div></Table.Cell
						>
					</Table.Row>
				{/each}
			</Table.Root>
		</section>
	</Card.Content>
</Card.Root>
