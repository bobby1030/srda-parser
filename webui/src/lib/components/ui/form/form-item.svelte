<script>
	import { cn } from "$lib/utils";
	let className = undefined;
	export { className as class };
</script>

<div class={cn("space-y-2", className)} {...$$restProps}>
	<slot />
</div>
