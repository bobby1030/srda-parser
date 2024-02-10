<script>
	import { getFormField } from "formsnap";
	import { cn } from "$lib/utils";
	import { Label } from "$lib/components/ui/label";
	let className = undefined;
	export { className as class };
	const { errors, ids } = getFormField();
</script>

<Label for={$ids.input} class={cn($errors && "text-destructive", className)} {...$$restProps}>
	<slot />
</Label>
