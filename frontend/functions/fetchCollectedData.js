import baseUrl from "./baseUrl";

export default async function(urlid, context) {
    const token = context.getters.getAuthToken;
    const esk = context.getters.getExclusiveStartKey(urlid);
    context.$axios.setHeader('token', token);
    context.$axios.setHeader('Content-Type', 'application/json')
    const eskString = esk ? `&lek=${esk}` : '';
    const response = await context.$axios.$get(
      `${baseUrl}/tpoints?urlid=${urlid}${eskString}`
    );
    if(response.STATUS == "OK") {
        if(response.LEK) context.dispatch('updateExclusiveStartKey', { urlid: urlid, exclusiveStartKey: response.LEK })
        else context.dispatch('updateExclusiveStartKey', { urlid: urlid, exclusiveStartKey: undefined })
        return response.DATA;
    }
}