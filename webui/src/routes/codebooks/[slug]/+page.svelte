<script>
    import * as Table from '$lib/components/ui/table';
    import * as Card from '$lib/components/ui/card';
    import { goto } from '$app/navigation';
    export let data;
</script>

<h1 class="text-3xl m-3">Codebook Details</h1>

<Card.Root>
	<Card.Header>
		<Card.Description>
			<span class="inline-block">{data.codebook.date}</span>
		</Card.Description>
		<Card.Title>{data.codebook.title}</Card.Title>
	</Card.Header>
	<Card.Content>
        <section class="p-3">
            <h3 class="font-semibold">Variables: {data.codebook.variables.length}</h3>
            <Table.Root>
                <Table.Header>
                    <Table.Row>
                        <Table.Head>Name</Table.Head>
                        <Table.Head>Description</Table.Head>
                        <Table.Head>Values</Table.Head>
                    </Table.Row>
                </Table.Header>
            
                {#each data.codebook.variables as variable}
                    <Table.Row class="hover:cursor-pointer" on:click={goto(`/variables/${variable.id}`)}>
                        <Table.Cell><span class="bg-secondary rounded-sm px-1.5 py-0.5 font-mono">{variable.name}</span></Table.Cell>
                        <Table.Cell>{variable.description}</Table.Cell>
                        <Table.Cell><div class="whitespace-pre-line max-h-12 overflow-y-scroll">{variable.values}</div></Table.Cell>
                    </Table.Row>
                {/each}
            </Table.Root>
        </section>
	</Card.Content>
</Card.Root>