export default async function(context){
    if(context.$store.state.isLoggedIn){
        context.$router.push('/dashboard')
    }
}