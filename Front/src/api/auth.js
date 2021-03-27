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
    return axios.get(`http://213.232.228.115/posts/`)
        .then(function (response) {
            return response.data
        })
        .catch(function (error) {
            console.log(error)
            return false
        })
}

export function sendScroll() {
    return axios.post(`https://3f3d33749f7e.ngrok.io/api/rating`,
        {
            headers: {
                session: localStorage.getItem('session')
            }
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
