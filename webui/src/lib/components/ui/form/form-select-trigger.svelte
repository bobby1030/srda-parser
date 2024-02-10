<script>
	import * as Select from "$lib/components/ui/select";
	import { getFormField } from "formsnap";
	const { attrStore, value } = getFormField();
	export let placeholder = "";
</script>

<Select.Trigger {...$$restProps} {...$attrStore} on:click on:keydown type="button">
	<slot value={$value}>
		<Select.Value {placeholder} />
	</slot>
</Select.Trigger>
