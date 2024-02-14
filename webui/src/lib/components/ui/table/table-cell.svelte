<script>
	import { cn } from '$lib/utils';
	import { goto } from '$app/navigation';
	let className = undefined;
	export { className as class };
	export let href;

	function handleClick() {
		if (href) {
			goto(href);
		}
	}
</script>

<td
	class={cn('p-2 align-middle [&:has([role=checkbox])]:pr-0', className)}	
	class:hover:cursor-pointer={href}
	on:click={handleClick}
	
	{...$$restProps}
>
	<slot />
</td>
