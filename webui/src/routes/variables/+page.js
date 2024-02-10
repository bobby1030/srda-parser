export async function load({ fetch, params }) {
	let variables = await fetch('/api/variables/').then((res) => res.json());

	return {
		variables
	};
}
