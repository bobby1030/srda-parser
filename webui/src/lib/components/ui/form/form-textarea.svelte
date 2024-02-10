<script>
	import { getFormField } from "formsnap";
	import { Textarea } from "$lib/components/ui/textarea";
	const { attrStore, value } = getFormField();
</script>

<Textarea
	{...$attrStore}
	bind:value={$value}
	{...$$restProps}
	on:blur
	on:change
	on:click
	on:focus
	on:keydown
	on:keypress
	on:keyup
	on:mouseover
	on:mouseenter
	on:mouseleave
	on:paste
	on:input
/>
