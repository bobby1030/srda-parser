<script>
	import { getFormField } from "formsnap";
	import * as RadioGroup from "$lib/components/ui/radio-group";
	const { attrStore, setValue, name, value } = getFormField();
	export let onValueChange = undefined;
</script>

<RadioGroup.Root
	{...$attrStore}
	onValueChange={(v) => {
		onValueChange?.(v);
		setValue(v);
	}}
	{...$$restProps}
>
	<slot />
	<input hidden {name} value={$value} />
</RadioGroup.Root>
