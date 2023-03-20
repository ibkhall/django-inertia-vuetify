import { createApp, h } from 'vue';
import { createInertiaApp } from '@inertiajs/inertia-vue3';
import { InertiaProgress } from '@inertiajs/progress';
import axios from 'axios';
import '../css/style.css';
import Layout from './layouts/Guest.vue';
import Authenticated from './layouts/Authenticated.vue';
import vuetify from './plugins/vuetify';

const pages = import.meta.glob('./pages/**/*.vue');

document.addEventListener('DOMContentLoaded', () => {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

    InertiaProgress.init({ showSpinner: true });

    createInertiaApp({
        resolve: async name => {
            console.log(name)
            const page = (await pages[`./pages/${name}.vue`]()).default;
            name=='Auth/Login' ? page.layout = page.layout || Layout : page.layout = page.layout || Authenticated;
            return page;
        },
        setup({ el, App, props, plugin }) {
            createApp({render: () => h(App, props)})
                .use(plugin)
                .use(vuetify)
                .mount(el)
        },
    });
});