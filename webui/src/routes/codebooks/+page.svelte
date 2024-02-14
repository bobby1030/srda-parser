<script>
	import * as Table from '$lib/components/ui/table';
	import * as Card from '$lib/components/ui/card';
	export let data;
</script>

<h1 class="m-3 text-3xl">Codebooks</h1>

<section class="flex">
	<Card.Root class="mx-5">
		<Card.Header>
			<Card.Title>人力運用調查</Card.Title>
		</Card.Header>

		<Card.Content>
			{#each data.codebooks as codebook}
				<a class="block hover:underline" href={`/codebooks/${codebook.id}`}>
                    {codebook.title}（{codebook.date}）
                </a>
			{/each}
		</Card.Content>
	</Card.Root>

	<Card.Root class="h-12 flex justify-center items-center">
        <p class="p-4">More codebooks coming soon...</p>
	</Card.Root>
</section>
