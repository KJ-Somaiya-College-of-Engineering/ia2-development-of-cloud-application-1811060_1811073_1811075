import verifyTokenAndGetUser from '@/functions/verifyTokenAndGetUser'
import getSpecificUrlDetails from '@/functions/getSpecificUrlDetails'
import fetchCollectedData from '@/functions/fetchCollectedData'

export const state = () => ({
    user: undefined,
    isLoggedIn: false,
    authToken: undefined,
    urls: [],
    collectedData: {},
    exclusiveStartKeys: {},
    update: 0,
    activeUrlObject: undefined,
    isMonitorLoading: false,
    isUrlDetailLoading: false
})

export const mutations = {
    SET_USER(state, user) {
        state.user = user;
        state.isLoggedIn = true;
    },
    SET_TOKEN(state, token) {
        state.authToken = token;
    },
    APPEND_URL_OBJECT(state, object) {
        state.urls.splice(0, 0, object);
    },
    CHANGE_URL_ARRAY(state, urlsArray) {
        state.urls = urlsArray;
    },
    REVERT_STATE_TO_ORIGINAL(state) {
        state.user = undefined
        state.isLoggedIn = false;
        state.authToken = undefined;
        state.urls = [];
        state.collectedData = undefined;
        state.exclusiveStartKeys = undefined;
        state.isMonitorLoading = false;
        state.isUrlDetailLoading = false;
    },
    UPDATE_COLLECTED_DATA(state, { urlid, collectedData }) {
        if(state.collectedData[urlid]){
            state.collectedData[urlid] = state.collectedData[urlid].concat(collectedData);
            state.update++;
            return;
        } else {
            state.collectedData[urlid] = collectedData
        }
        state.update ++;
    },
    UPDATE_EXCLUSIVE_START_KEY(state, { urlid, exclusiveStartKey }) {
        state.exclusiveStartKeys[urlid] = exclusiveStartKey;
        state.update++
    },
    SET_ACTIVE_URL_OBJECT(state, object) {
        state.activeUrlObject = object;
    },
    SET_MONITOR_LOADING_STATUS(state, value) {
        state.isMonitorLoading = value;
    },
    SET_URL_DETAIL_LOADING_STATUS(state, value) {
        state.isUrlDetailLoading = value;
    },
    DELETE_URL_ELEMENT(state, value){
        var index = 0;
        var found = false;
        for(index = 0; index < state.urls?.length; index++){
            if(state.urls[index]._id == value) {
                found = true;
                break;
            }
        }
        if(found)
        state.urls.splice(index, 1);
    }
}

export const actions = {
    async fetchAndSetUser(context) {
        const token = localStorage.getItem("token");
        if(token){
            const user = await verifyTokenAndGetUser(token, this);
            context.commit("SET_USER", user);
            context.commit('SET_TOKEN', token);
        }
    },
    updateUserAndToken(context, {user, token}) {
        localStorage.setItem("token", token)
        if(token) {
            context.commit("SET_USER", user);
            context.commit('SET_TOKEN', token);
        }
    },
    addNewShortedUrlObject(context, object) {
        context.commit('APPEND_URL_OBJECT', object);
    },
    updateUrls(context, urlsArray) {
        context.commit('CHANGE_URL_ARRAY', urlsArray);
    },
    cleanupAndLogout(context) {
        localStorage.removeItem("token");
        context.commit('REVERT_STATE_TO_ORIGINAL')
    },
    async fetchNextPage(context, {urlid, first}) {
        context.commit('SET_MONITOR_LOADING_STATUS', true);
        if(first) {
            if(this.getters.wasInitiallyLoaded(urlid)) return;
        }
        const data = await fetchCollectedData(urlid, this);
        if(data){
            context.commit('UPDATE_COLLECTED_DATA', { urlid: urlid, collectedData: data });
        }
        context.commit('SET_MONITOR_LOADING_STATUS', false);
    },
    updateExclusiveStartKey(context, { urlid, exclusiveStartKey }) {
        context.commit('UPDATE_EXCLUSIVE_START_KEY', { urlid, exclusiveStartKey });
    },
    
    async fetchSpecificUrl(context, urlid) {
        context.commit('SET_URL_DETAIL_LOADING_STATUS', true)
        const data = await getSpecificUrlDetails(urlid, this)
        if(data){
            context.commit('SET_ACTIVE_URL_OBJECT', data)
        }
        context.commit('SET_URL_DETAIL_LOADING_STATUS', false)
    },
    deleteUrlEntry(context, urlid){
        context.commit("DELETE_URL_ELEMENT", urlid)
    }
}

export const getters = {
    getAuthToken(state) {
        if(state.authToken) return state.authToken;
        const tempToken = localStorage.getItem('token');
        if(tempToken) return tempToken;
    },
    getUrlDetails(state) {
        return async function(urlid) {
            const urlObj = state.urls.find((url) => url._id == urlid)
            if(urlObj) return urlObj;
        }
    },
    getExclusiveStartKey(state) {
        return function (urlid) {
            if(state.exclusiveStartKeys)
                return state.exclusiveStartKeys[urlid];
        }
    },
    hasMorePages(state) {
        return function (urlid) {
            if(state.exclusiveStartKeys[urlid]) return true;
            return false;
        }
    },
    getDataPointsArray(state) {
        return function (urlid) {
            if(state.collectedData) return state.collectedData[urlid];
        }
    },
    wasInitiallyLoaded(state) {
        return function (urlid) {
            if(state.collectedData[urlid]) return true;
            return false;
        }
    }
}