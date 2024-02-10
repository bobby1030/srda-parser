<script>
	import * as Button from "$lib/components/ui/button";
</script>

<Button.Root type="submit" {...$$restProps} on:click on:keydown>
	<slot />
</Button.Root>
