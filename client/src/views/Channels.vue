<template>
    <v-container fluid grid-list-xl>
        <h1>{{name}}</h1>
        <v-layout wrap justify-space-around>
            <v-flex v-for="chanel in channels">
                <router-link :to="channel/channel.nickname">
                    <v-card class="mx-auto" max-width="344" outlined tile>
                        <v-list-item three-line>
                            <v-list-item-content>
                                <div class="overline mb-4">channel.nickname</div>
                                <v-list-item-title class="headline mb-1">channel.hub</v-list-item-title>
                                <v-list-item-subtitle>channel.desc
                                </v-list-item-subtitle>
                            </v-list-item-content>

                            <v-list-item-avatar tile size="80" color="grey"></v-list-item-avatar>
                        </v-list-item>
                        <v-card-actions>
                        </v-card-actions>
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
                name
            }
        },
        methods: {
            async getChannels() {
                await axios.get('http://localhost:5000/channels?hub=' + window.location.href.split('/')[4])
                    .then((res) => {
                        this.channels = res.data;
                        console.log(res.data)
                    })
            },
            getName(){
                let url = window.location.href;
                const capitalize = (s) => {
                    if (typeof s !== 'string') return '';
                    return s.charAt(0).toUpperCase() + s.slice(1);
                }
                this.name = capitalize(url.split('/')[4]);
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
