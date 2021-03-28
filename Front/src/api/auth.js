const axios = require('axios')

export function getFilters() {
    return axios.get(`http://213.232.228.115/filters/`)
        .then(function (response) {
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getPosts() {
    return axios.get(`http://213.232.228.115/posts/`,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function getPost(id) {
    return axios.get(`http://213.232.228.115/posts/` + id,
        {
            headers: {
                session: localStorage.getItem('session')
            }
        })
        .then(function (response) {
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function sendScroll(data) {
    return axios.post(`http://213.232.228.115/statistics/`, JSON.stringify(data),
        {
            headers: {
                session: localStorage.getItem('session')
            },
        })
        .then(function (response) {
            console.log(response)
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}
