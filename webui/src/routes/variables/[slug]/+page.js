export async function load({ fetch, params }) {
	let variable_id = params.slug;
    
    let variable = await fetch(`/api/variables/${variable_id}`).then(res => res.json());

	let similar = await fetch(`/api/variables/similar/${variable_id}?limit=30`).then(res => res.json());

	return {
        variable,
		similar
	};
}
