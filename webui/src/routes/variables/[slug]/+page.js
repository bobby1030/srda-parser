export async function load({ fetch, params }) {
	let variable_id = params.slug;
    
    let variable = await fetch(`/api/variables/${variable_id}`).then(res => res.json());

	let similar = await fetch(`/api/variables/similar/${variable_id}?limit=10`).then(res => res.json());
	let similar_across_codebooks = await fetch(`/api/variables/similar/across-codebooks/${variable_id}`).then(res => res.json());

	return {
        variable,
		similar,
		similar_across_codebooks
	};
}
