<script>
	import { Form as FormPrimitive } from "formsnap";
	import { cn } from "$lib/utils";
	let className = undefined;
	export { className as class };
</script>

<FormPrimitive.Validation
	class={cn("text-sm font-medium text-destructive", className)}
	{...$$restProps}
/>
