import type { RootScreenProps } from '@/navigation';
import { useTranslation } from 'react-i18next';
import { ScrollView, Text, View, TouchableOpacity } from 'react-native';
import { useTheme } from '@/theme';
import { SafeScreen } from '@/components/templates';
import { Paths } from '@/navigation/paths';

function Settings({ navigation }: RootScreenProps<Paths.Settings>) {
    const { t } = useTranslation();

    const {
        backgrounds,
        fonts,
        gutters,
        layout,
    } = useTheme();

    return (
        <SafeScreen>
            <View
                style={[
                    layout.row,
                    layout.justifyStart,
                    backgrounds.white,
                    gutters.paddingHorizontal_16,
                    gutters.marginTop_16,
                ]}

            >
            <TouchableOpacity
                onPress={() => {
                   navigation.navigate(Paths.Home);
                }}
            >
            <Text style={[fonts.size_16, fonts.gray800 ]}>
                {t('screen_settings.back_button')}
            </Text>

            </TouchableOpacity>
            </View>
            <ScrollView>
                <View
                    style={[
                        layout.justifyCenter,
                        layout.itemsCenter,
                        gutters.marginTop_80,
                    ]}
                >
                    <View style={[layout.absolute, gutters.paddingTop_40]}>
                        <Text style={[fonts.size_40, fonts.gray800, fonts.bold]}>
                            {t('screen_settings.title')}
                        </Text>
                    </View>
                </View>
            </ScrollView>
        </SafeScreen>
    );
}

export default Settings;
