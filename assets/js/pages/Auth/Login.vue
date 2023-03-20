<script setup>
import { Inertia } from '@inertiajs/inertia';
import { Head, Link, useForm } from '@inertiajs/inertia-vue3';
import { mdiAccount,mdiLogin } from '@mdi/js'



defineProps({
    canResetPassword: Boolean,
    status: String,
});

const form = useForm({
    username: '',
    password: ''
});

const submit = () => {
    form.post('/auth/connect', {
        headers: {
            'X-CSRFToken': document.querySelector("meta[name='csrf-token']").content
        }
    })
    
};

const imgUrl = new URL('../../dankanka.png', import.meta.url).href
</script>

<template>
   
    <Head title="Log in" />
    
    <v-row  align-content="center" justify-content="center" align="center" justify="center" class="mt-10">
        <v-col align-self="center" md="3">
            <v-card>
                <v-card-title class="text-center text-primary text-h5 font-weight-bold">Authentification</v-card-title>
                <v-card-text>
                    <v-img class="mx-auto mb-10" width="150" :src="imgUrl"></v-img>
                    <v-form @submit.prevent="submit">
                    <v-text-field 
                        v-model="form.username"
                        color="primary" 
                        variant="outlined" 
                        label="Username" 
                        :error-messages="form.errors.username"
                    ></v-text-field>
                    <v-text-field 
                        v-model="form.password" 
                        color="primary" 
                        variant="outlined" 
                        type="password" 
                        label="Mot de passe"
                    ></v-text-field>
                    <v-checkbox
                        color="primary" 
                        v-model="form.remember" 
                        hide-details label="Se souvenir de moi"
                    ></v-checkbox>
                    <v-btn type="submit" :icon="mdiSignDirection" block color="primary">
                        <v-icon start :icon="mdiLogin"></v-icon>
                        Connexion</v-btn>
                </v-form>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
   
</template>
