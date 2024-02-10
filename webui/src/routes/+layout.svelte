<script>
	import '../app.pcss';
	import { page } from '$app/stores';
	export let data;
</script>

<nav>
	<ul class="border-b-2 p-4">
		<a class="mx-2" href="/">SRDA Explorer</a>
		{#each data.sections as section}
			<a
				class="text-foreground/60 hover:text-foreground/80 mx-2"
				class:text-foreground={$page.url.pathname === section.route}
				href={section.route}
			>
				{section.title}
			</a>
		{/each}
	</ul>
</nav>

<main class="container mx-auto py-4">
	<slot />
</main>
