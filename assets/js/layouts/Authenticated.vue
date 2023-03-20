<script setup>
import { ref } from 'vue';
import { mdiAccount, mdiSquareMedium, mdiViewDashboard, mdiAccountCircle, mdiCogs, mdiCogOutline, mdiBrain, mdiChevronUp, mdiChevronDown } from '@mdi/js';

import { Link } from '@inertiajs/inertia-vue3';

const cruds = [
    ['Liste de produits', mdiSquareMedium],

]

let drawer = ref(true);
let open = ref("Users");
const imgUrl = new URL('../dankanka.png', import.meta.url).href
const bgUrl = new URL('../bg.jpeg', import.meta.url).href
const maleImg = new URL('../male.png', import.meta.url).href

const navigate = function() {}

</script>

<template>
    <v-app>
        <v-navigation-drawer width="280" app v-model="drawer">
            <v-toolbar dense color="primary">
                <v-list-item
                title="Ets Dankanka"
                >
                
                    <template v-slot:prepend>
                    <v-avatar>
                        <v-img width="80" :src="imgUrl"></v-img>
                    </v-avatar>
                    </template>
                </v-list-item>
            </v-toolbar>
            <v-card class="" flat :image="bgUrl" height="150">
                <v-list-item
                class="mt-10"
                color="primary"
                title="John Doe"
                subtitle="Administrateur"
                >
                
                    <template v-slot:prepend>
                    <v-avatar>
                        <v-img alt="profile"
                        width="30"
                            :src="maleImg">
                        </v-img>
                    </v-avatar>
                    </template>
                </v-list-item>
               
            </v-card>
            <v-list v-model:opened="open" nav>
                <v-list-item @click.prevent="$inertia.visit('/home')" href="/home" link active active-color="primary"  rounded  v-ripple class="text-grey-darken-3" :prepend-icon="mdiViewDashboard" title="Tableau de bord"></v-list-item>
                <v-list-group fluid :collapse-icon="mdiChevronUp" :expand-icon="mdiChevronDown">
                    <template v-slot:activator="{ props }">
                        <v-list-item nav rounded v-ripple v-bind="props" :prepend-icon="mdiCogs" title="Paramètres" value="Configs">
                        </v-list-item>
                    </template>

                    <v-list-group class="ml-7" fluid :collapse-icon="mdiChevronUp" :expand-icon="mdiChevronDown">
                        <template v-slot:activator="{ props }">
                            <v-list-item  :prepend-icon="mdiSquareMedium" rounded v-ripple v-bind="props" title="Produits" value="Products">
                            </v-list-item>
                        </template>
                        
                        <v-list-item rounded v-ripple v-for="([title, icon], i) in cruds" :key="i" :value="title" :title="title">
                        <template v-slot:prepend>
                            <v-icon class="ml-7" start :icon="icon"></v-icon>
                        </template>
                    </v-list-item>
                    </v-list-group>
                <v-list-item active-color="primary"  rounded  v-ripple class="text-grey-darken-3 ml-7" :prepend-icon="mdiSquareMedium" title="Opérateurs"></v-list-item>

                </v-list-group>
            </v-list>
            <!-- -->
        </v-navigation-drawer>

        <v-app-bar app color="primary">
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

            <v-spacer></v-spacer>

            <v-menu>
                 <template v-slot:activator="{ props }">
                    <v-btn
                    color="primary"
                    v-bind="props"
                
                    >
                    <v-avatar item size="32px">
                            <v-img alt="user" :src="maleImg"></v-img>
                        </v-avatar>
                    </v-btn>
                </template>
            
                <v-card outlined  tile color="indigo">
                    <v-row align="center" justify="center">
                        <v-col cols="12">
                            <v-avatar class="profile" color="grey" size="100" tile>
                                <v-img class="mx-auto" :src="maleImg"></v-img>
                            </v-avatar>
                        </v-col>
                        <v-col>
                            
                                <v-list-item>
                            <v-list-item-title>Content filtering</v-list-item-title>

                            <v-list-item-subtitle>
                           Administrateur
                            </v-list-item-subtitle>
                            </v-list-item>
                            
                        </v-col>
                    </v-row>
                </v-card>

                <v-list dense>
                    <v-list-item-group color="primary">
                        <v-list-item rounded v-ripple class="text-grey-darken-3" :prepend-icon="mdiAccount" title="Mon Profil"></v-list-item>
                        <v-list-item rounded v-ripple class="text-grey-darken-3" :prepend-icon="mdiAccount" title="Changement de mot de passe"></v-list-item>
                        <v-list-item rounded v-ripple class="text-grey-darken-3" :prepend-icon="mdiAccount" title="Déconnexion"></v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-menu>
        </v-app-bar>
        <v-main>
            <v-container fluid>
                <slot />
            </v-container>
        </v-main>

        <v-footer app absolute dark color="primary" class="font-weight-medium">

            {{ new Date().getFullYear() }} © <small class="d-inline-block ml-2"> Ets Dankanka</small>
            <v-spacer></v-spacer>
            <span class="font-weight-light">Made with ❤️ by SYNETCOM</span>
        </v-footer>
    </v-app>
</template>