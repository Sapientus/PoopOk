<template>
    <div class="flex flex-col items-center  justify-center bg-white dark:bg-gray-900 shadow-lg shadow-bg-gray-800 p-6 mb-10 rounded-lg">
        <h1 class="text-2xl font-semibold text-gray-800 dark:text-gray-100">
            {{ t("resetPassword") }}
        </h1>
        <div class="text-gray-800 dark:text-gray-100 text-[13px] mt-2 text-center">
            {{ t("resetPasswordDescription") }}
        </div>
    </div>
    <form>
        <div class="relative">
            <label for="email" class="text-gray-800 dark:text-gray-100 text-[13px] bg-white dark:bg-gray-800 absolute px-2 top-[-9px] left-[18px] font-semibold z-10">
                {{ t("email") }}
            </label>
            <div class="my-4">
                <BaseInput
                    name="email"
                    v-model="email"
                    autocomplete="email"
                    placeholder="name@mail.com"
                    required
                />
            </div>
        </div>
        <div>
            <BaseButton type="submit">
                {{ t("resetPassword") }}
            </BaseButton>
        </div>
    </form>
</template>

<script setup>
import { ref } from "vue";
import { useI18n } from "vue-i18n";
import BaseInput from "@/UI/BaseInput.vue";
import BaseButton from "@/UI/BaseButton.vue";

const { t } = useI18n();

const email = ref("");

const resetPassword = () => {
    console.log(email.value);
};


</script>