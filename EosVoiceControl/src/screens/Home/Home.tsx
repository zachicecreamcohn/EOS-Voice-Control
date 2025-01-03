import type { RootScreenProps } from '@/navigation/types';
import { useTranslation } from 'react-i18next';
import { ScrollView, Text, View, TouchableOpacity } from 'react-native';
import { IconByVariant } from '@/components/atoms';
import { useTheme } from '@/theme';
import { Paths } from '@/navigation/paths';
import { SafeScreen } from '@/components/templates';
import { useNavigation } from '@react-navigation/native';

function Home({ navigation }: RootScreenProps) {
    const { t } = useTranslation();

    const {
        backgrounds,
        colors,
        fonts,
        gutters,
        layout,
    } = useTheme();

    return (
        <SafeScreen>
            <View
                style={[
                    layout.row,
                    layout.justifyEnd,
                    backgrounds.white,
                    gutters.paddingHorizontal_16,
                    gutters.marginTop_16,
                ]}

            >
            <TouchableOpacity
                onPress={() => {
                    navigation.navigate(Paths.Settings);
                }}
            >
            <IconByVariant
                path={"settings"}
                color={colors.orange}

            />

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
                            {t('screen_home.title')}
                        </Text>
                        <Text style={[fonts.size_16, fonts.orange, gutters.paddingTop_8]}>
                            {t('screen_home.name_tag')}
                        </Text>
                    </View>
                </View>
            </ScrollView>
        </SafeScreen>
    );
}

export default Home;
