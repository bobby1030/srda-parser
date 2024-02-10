<script>
	import * as Select from "$lib/components/ui/select";
	import { getFormField } from "formsnap";
	const { setValue, name, value } = getFormField();
	export let onSelectedChange = undefined;
</script>

<Select.Root
	onSelectedChange={(v) => {
		onSelectedChange?.(v);
		setValue(v ? v.value : undefined);
	}}
	{...$$restProps}
>
	<slot />
	<input hidden {name} value={$value} />
</Select.Root>
