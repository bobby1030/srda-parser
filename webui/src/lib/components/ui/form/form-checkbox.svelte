<script>
	import { getFormField } from "formsnap";
	import { Checkbox } from "$lib/components/ui/checkbox";
	export let onCheckedChange = undefined;
	const { name, setValue, attrStore, value } = getFormField();
	const { name: nameAttr, value: valueAttr, ...rest } = $attrStore;
</script>

<Checkbox
	{...rest}
	checked={typeof $value === "boolean" ? $value : false}
	onCheckedChange={(v) => {
		onCheckedChange?.(v);
		setValue(v);
	}}
	{...$$restProps}
	on:click
	on:keydown
/>
<input hidden {name} value={$value} />
