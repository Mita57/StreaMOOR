<template>
    <v-container fluid grid-list-xl>
        <h1>{{name}}</h1>
        <v-layout wrap justify-space-around>
            <v-flex v-for="chanel in channels">
                <router-link :to="getUrl(chanel[0])">
                    <v-card class="mx-auto" max-width="344" outlined>
                        <v-list-item three-line>
                            <v-list-item-content>
                                <div class="overline mb-4"></div>
                                <v-list-item-title class="headline mb-1">{{chanel[0]}}</v-list-item-title>
                                <v-list-item-subtitle>{{chanel[2]}}</v-list-item-subtitle>
                            </v-list-item-content>
                            <v-list-item-avatar tile size="80" color="grey"><img src="../assets/Igor.png"></v-list-item-avatar>
                        </v-list-item>
                    </v-card>
                </router-link>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Channels",
        data() {
            return {
                channels: [],
                name: '',
            }
        },
        methods: {
            async getChannels() {
                const rw = this;
                await axios.get('http://localhost:5000/channels?hub=' + window.location.href.split('/')[4])
                    .then(function (res) {
                        rw.channels = res.data;
                    })
                    .catch(function (res) {
                        //handle error
                        console.log(res);
                    })
            },
            getName() {
                let url = window.location.href;
                const capitalize = (s) => {
                    if (typeof s !== 'string') return '';
                    return s.charAt(0).toUpperCase() + s.slice(1);
                }
                this.name = capitalize(url.split('/')[4]);
            },
            getUrl(nick) {
                let url = window.location.href;
                let name = (url.split('/')[4]);
                return (name + '/' + nick);
            }

        },
        created() {
            this.getChannels();
            this.getName();
        }
    }

</script>

<style scoped>

</style>
