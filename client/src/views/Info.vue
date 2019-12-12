<template>
    <div id="land">
        <section>
            <v-layout align-center="" class=" mt-4" column wrap >
                <v-flex xs12>
                    <v-container grid-list-xl >
                        <v-layout justify-space-around="" row wrap >
                            <v-flex md4 xs12>
                                <h1 class="mb-4 text-ju">Новое слово на рынке интернет-вещания</h1>
                               <p class="text-justify"> Сервис StreaMOOR позволяет осуществлять онлайн транслацию на высоком уровне  с интерактивным
                                взаимодействием со зрителями. Также онлайн-трансляции разделены на хабы, таким образом
                                   идет группировка каналов по интересам и это облегчает поиск интересующих вас каналов.</p>
                                <h1 class="mb-4 mt-4">Зачем это нужно?</h1>
                                <p class="text-justify">С распростанением интернета все больше людей хотят делиться
                                моментами из своей жизни, или делиться с окружающими своими мыслями или знаниями. </p>
                                <v-btn x-large tile dark class="blue mt-4" to = "/register" v-if="user=='Войти'">Создать аккаунт</v-btn>
                            </v-flex>
                            <v-flex mr4 xs5  class="d-flex" justify="space-around">
                                <v-flex>
                                    <v-img :src="require('../assets/pic1.jpg')" />
                                    <v-img :src="require('../assets/pic3.jpg')" class="mt-4"  />
                                </v-flex>
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-flex>
            </v-layout>
        </section>
    </div>

</template>

<script>
</script>

<style scoped>

</style>
