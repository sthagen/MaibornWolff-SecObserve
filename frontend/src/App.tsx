import { Route } from "react-router";
import { Admin, CustomRoutes, Resource } from "react-admin";
import polyglotI18nProvider from "ra-i18n-polyglot";

import authProvider from "./access_control/authProvider";
import { Dashboard } from "./dashboard";

import englishMessages from "./commons/i18n/en";
import { Layout } from "./commons/layout";
import { Login } from "./access_control";
import { getTheme } from "./commons/settings/functions";
import Settings from "./commons/settings/Settings";
import drfProvider from "./commons/ra-data-django-rest-framework";

import products from "./core/products";
import observations from "./core/observations";
import parsers from "./core/parsers";
import general_rules from "./rules/general_rules";
import evidences from "./core/evidences";

const i18nProvider = polyglotI18nProvider(() => {
    return englishMessages;
}, "en");

const App = () => {
    return (
        <Admin
            title=""
            dataProvider={drfProvider()}
            authProvider={authProvider}
            dashboard={Dashboard}
            loginPage={Login}
            layout={Layout}
            i18nProvider={i18nProvider}
            disableTelemetry
            theme={getTheme()}
        >
            <CustomRoutes>
                <Route path="/settings" element={<Settings />} />
            </CustomRoutes>
            <Resource
                name="products"
                {...products} // nosemgrep: typescript.react.best-practice.react-props-spreading.react-props-spreading
                // nosemgrep because the props are well defined in the import
                recordRepresentation={(record) => `${trim_string(record.name)}`}
            />
            <Resource
                name="observations"
                {...observations} // nosemgrep: typescript.react.best-practice.react-props-spreading.react-props-spreading
                // nosemgrep because the props are well defined in the import
                recordRepresentation={(record) =>
                    `${trim_string(record.title)}`
                }
            />
            <Resource
                name="parsers"
                {...parsers} // nosemgrep: typescript.react.best-practice.react-props-spreading.react-props-spreading
                // nosemgrep because the props are well defined in the import
                recordRepresentation={(record) => `${trim_string(record.name)}`}
            />
            <Resource
                name="general_rules"
                {...general_rules} // nosemgrep: typescript.react.best-practice.react-props-spreading.react-props-spreading
                // nosemgrep because the props are well defined in the import
                recordRepresentation={(record) => `${trim_string(record.name)}`}
            />
            <Resource
                name="product_rules"
                recordRepresentation={(record) => `${trim_string(record.name)}`}
            />
            <Resource
                name="evidences"
                {...evidences} // nosemgrep: typescript.react.best-practice.react-props-spreading.react-props-spreading
                // nosemgrep because the props are well defined in the import
                recordRepresentation={(record) => `${trim_string(record.name)}`}
            />
        </Admin>
    );
};

function trim_string(in_string: string) {
    const out_string =
        in_string.length > 50 ? in_string.substring(0, 50) + "..." : in_string;

    return out_string;
}

export default App;
