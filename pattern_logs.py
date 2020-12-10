# coding:utf-8


def get_pattern_logs(module, log_type_desc):
    pattern_logs = None

    if module == "AAA":

        if log_type_desc == "AAA_SUCCESS":
            pattern_logs = \
                [{'patterns': ['AAA succeeded.'], 'log_explanation': '接受用户的AAA请求', 'log_recommended_action': '无'}]


    elif module == "ACL":

        if log_type_desc == "ACL_ACCELERATE_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to accelerate %{DATA:aclType} ACL %{NUMBER:aclNumber:int}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统加速ACL失败',
                             'log_recommended_action': '删除一些规则或者关闭其他ACL的加速功能，释放硬件资源'}]

        elif log_type_desc == "ACL_ACCELERATE_NONCONTIGUOUSMASK":
            pattern_logs = [{'patterns': [
                'Failed to accelerate ACL %{NUMBER:aclNumber:int}. ACL acceleration supports only contiguous wildcard masks.'],
                             'log_explanation': '因IPv4 ACL中的规则指定了非连续的掩码，导致ACL加速失败',
                             'log_recommended_action': '检查ACL规则并删除不支持的配置'}]

        elif log_type_desc == "ACL_ACCELERATE_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'Failed to accelerate %{DATA:aclType} ACL %{NUMBER:aclNumber:int}. The operation is not supported.'],
                             'log_explanation': '因系统不支持ACL加速而导致ACL加速失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "ACL_ACCELERATE_NOT_SUPPORTHOPBYHOP":
            pattern_logs = [{'patterns': [
                'Failed to accelerate IPv6 ACL %{NUMBER:aclNumber:int}. ACL acceleration does not support the rules that contain the hop-by-hop keywords.'],
                             'log_explanation': '因IPv6 ACL中的规则指定了hop-by-hop参数，导致ACL加速失败',
                             'log_recommended_action': '检查ACL规则并删除不支持的配置'}]

        elif log_type_desc == "ACL_ACCELERATE_NOT_SUPPORTMULTITCPFLAG":
            pattern_logs = [{'patterns': [
                'Failed to accelerate IPv6 ACL %{NUMBER:aclNumber:int}. ACL acceleration does not support specifying multiple TCP flags in one rule.'],
                             'log_explanation': '因IPv6 ACL中的规则指定了多个Tcp Flag参数，导致ACL加速失败',
                             'log_recommended_action': '检查ACL规则并删除不支持的配置'}]

        elif log_type_desc == "ACL_ACCELERATE_UNK_ERR":
            pattern_logs = [{'patterns': ['Failed to accelerate %{DATA:aclType} ACL %{NUMBER:aclNumber:int}.'],
                             'log_explanation': '因系统故障导致ACL加速失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "ACL_IPV6_STATIS_INFO":
            pattern_logs = [{'patterns': [
                'IPv6 ACL %{NUMBER:aclNumber:int} %{DATA:idContentIpv6AclRule} %{NUMBER:numberPacketsMatchedRule:int} packet\\(s\\).'],
                             'log_explanation': '匹配上IPv6 ACL规则的报文数量发生变化', 'log_recommended_action': '无'}]

        elif log_type_desc == "ACL_NO_MEM":
            pattern_logs = [
                {'patterns': ['Failed to configure %{DATA:aclType} ACL %{NUMBER:aclNumber:int} due to lack of memory'],
                 'log_explanation': '内存不足导致配置ACL失败', 'log_recommended_action': '使用display memory-threshold命令检查内存使用情况'}]

        elif log_type_desc == "ACL_STATIS_INFO":
            pattern_logs = [{'patterns': [
                'ACL %{NUMBER:aclNumber:int} %{DATA:idContentIpv4AclRule} %{NUMBER:numberPacketsMatchedRule:int} packet\\(s\\).'],
                             'log_explanation': '匹配上IPv4 ACL规则的报文数量发生变化', 'log_recommended_action': '无'}]


    elif module == "ANCP":

        if log_type_desc == "ANCP_INVALID_PACKET":
            pattern_logs = [{'patterns': [
                'The %{DATA:field} value %{DATA:wrongValueField} is wrong, and the value %{DATA:expectedValueField} is expected.'],
                             'log_explanation': '系统收到一个错误的ANCP邻接报文，报文中指定字段与预期值不一致', 'log_recommended_action': '无需处理'}]


    elif module == "APMGR":

        if log_type_desc == "APMGR_AC_MEM_ALERT":
            pattern_logs = [{'patterns': ['The memory utilization has reached the threshold.'],
                             'log_explanation': '创建手工AP成功时触发，但由于达到内存门限值，AP不能上线',
                             'log_recommended_action': '此时不应该继续创建AP，且不允许有新AP上线'}]

        elif log_type_desc == " APMGR_ADD_AP_FAIL":
            pattern_logs = [{'patterns': [
                'AP %{DATA:apName} failed to come online using serial ID %{DATA:serialId}: MAC address %{DATA:macAddress} is being used by AP %{DATA:apName}.'],
                             'log_explanation': 'AP上线过程中，由于MAC地址已存在，添加MAC地址失败，AP不能上线',
                             'log_recommended_action': '将此AP的MAC地址或serial ID对应的手工AP删除一个，AP方能正常上线'}]

        elif log_type_desc == "APMGR_AP_OFFLINE":
            pattern_logs = [{'patterns': ['AP %{DATA:apName} went offline. State changed to Idle.'],
                             'log_explanation': 'AP下线，状态变为Idle状态',
                             'log_recommended_action': '·          若AP主动下线，则不用排查问题\n·          若AP异常下线，需要根据调试信息定位并解决问题'}]

        elif log_type_desc == "APMGR_AP_ONLINE":
            pattern_logs = [{'patterns': ['AP %{DATA:apName} went online. State changed to Run.'],
                             'log_explanation': 'AP上线，状态变为运行状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWC_IMG_DOWNLOAD_COMPLETE":
            pattern_logs = [{'patterns': [
                'System software image file %{DATA:imageFileName} downloading through the CAPWAP tunnel to AC %{DATA:acIpAddress} completed.'],
                             'log_explanation': 'AP从AC下载系统镜像成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWC_IMG_DOWNLOAD_START":
            pattern_logs = [{'patterns': [
                'Started to download the system software image file %{DATA:imageFileName} through the CAPWAP tunnel to AC %{DATA:acIpAddress}.'],
                             'log_explanation': 'AP开始进行版本文件下载', 'log_recommended_action': '保持AP和AC之间正常的网络连接使AP能够正常升级'}]

        elif log_type_desc == "APMGR_CWC_IMG_NO_ENOUGH_SPACE":
            pattern_logs = [{'patterns': [
                'Insufficient flash memory space for downloading system software image file %{DATA:imageFileName}.'],
                             'log_explanation': '由于AP上的Flash剩余空间不足导致AP进行版本升级不成功',
                             'log_recommended_action': '建议删除AP上无用的文件以进行版本升级'}]

        elif log_type_desc == "APMGR_CWC_LOCAL_AC_DOWN":
            pattern_logs = [{'patterns': [
                'CAPWAP tunnel to Central AC %{DATA:ipAddressCentralAc} went down. Reason: %{DATA:reason}.'],
                             'log_explanation': 'Central AC与Local AC之间隧道断开及断开原因',
                             'log_recommended_action': '·          检查Central AC与Local AC的连接是否正常\n·          检查Central AC上的配置\n·          检查Local AC上的配置'}]

        elif log_type_desc == "APMGR_CWC_LOCAL_AC_UP":
            pattern_logs = [{'patterns': ['CAPWAP tunnel to Central AC %{DATA:ipAddressCentralAc} went up.'],
                             'log_explanation': 'Central AC与Local AC建立CAPWAP隧道', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWC_REBOOT":
            pattern_logs = [{'patterns': ['AP in state %{DATA:apState} is rebooting. Reason: %{DATA:reason}'],
                             'log_explanation': 'AP重启及重启原因', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWC_RUN_DOWNLOAD_COMPLETE":
            pattern_logs = [{'patterns': [
                'File %{DATA:fileName} successfully downloaded through the CAPWAP tunnel to AC %{DATA:acIpAddress}.'],
                             'log_explanation': 'AP从AC下载文件成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWC_RUN_DOWNLOAD_START":
            pattern_logs = [{'patterns': [
                'Started to download the file %{DATA:fileName} through the CAPWAP tunnel to AC %{DATA:acIpAddress}.'],
                             'log_explanation': 'AP开始进行版本文件下载',
                             'log_recommended_action': '保持AP和AC之间都处于RUN状态，AC才能够正常下载文件到AP'}]

        elif log_type_desc == "APMGR_CWC_RUN_NO_ENOUGH_SPACE":
            pattern_logs = [{'patterns': ['Insufficient flash memory space for downloading file %{DATA:fileName}.'],
                             'log_explanation': '由于AP上的Flash剩余空间不足导致AP进行文件下载不成功',
                             'log_recommended_action': '建议删除AP上无用的文件以进行文件下载'}]

        elif log_type_desc == "APMGR_CWC_TUNNEL_DOWN":
            pattern_logs = [{'patterns': ['CAPWAP tunnel to AC %{DATA:acIpAddress} went down. Reason: %{DATA:reason}.'],
                             'log_explanation': 'AP与AC之间CAPWAP隧道断开以及断开原因',
                             'log_recommended_action': '请检查AP与AC之间的网络连接是否正常'}]

        elif log_type_desc == "APMGR_CWC_TUNNEL_UP":
            pattern_logs = [{'patterns': ['%{DATA:tunnelType} CAPWAP tunnel to AC %{DATA:acIpAddress} went up.'],
                             'log_explanation': 'AP成功连接到AC，即AP已进入Run状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_ CWS_IMG_DOWNLOAD_COMPLETE":
            pattern_logs = [{'patterns': [
                'System software image file %{DATA:imageFileName} downloading through the CAPWAP tunnel for AP %{DATA:apName} completed.'],
                             'log_explanation': 'AP已经成功完成版本文件下载', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWS_IMG_DOWNLOAD_START":
            pattern_logs = [{'patterns': [
                'AP %{DATA:apName} started to download the system software image file %{DATA:imageFileName}.'],
                             'log_explanation': 'AP开始进行版本文件下载', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWS_LOCAL_AC_DOWN":
            pattern_logs = [
                {'patterns': ['CAPWAP tunnel to local AC %{DATA:ipAddressLocalAc} went down. Reason: %{DATA:reason}.'],
                 'log_explanation': 'Central AC与Local AC之间隧道断开及断开原因',
                 'log_recommended_action': '·          检查Central AC与Local AC的连接是否正常\n·          检查Central AC上的配置\n·          检查Local AC上的配置'}]

        elif log_type_desc == "APMGR_CWS_LOCAL_AC_UP":
            pattern_logs = [{'patterns': ['CAPWAP tunnel to local AC %{DATA:ipAddressLocalAc} went up.'],
                             'log_explanation': 'Central AC与 Local AC建立CAPWAP隧道', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWS_RUN_DOWNLOAD_COMPLETE":
            pattern_logs = [{'patterns': [
                'File %{DATA:fileName} successfully downloaded through the CAPWAP tunnel for AP %{DATA:apName}.'],
                             'log_explanation': 'AP已经成功完成文件下载', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWS_RUN_DOWNLOAD_START":
            pattern_logs = [{'patterns': ['AP %{DATA:apName} started to download the file %{DATA:fileName}.'],
                             'log_explanation': 'AP开始进行配置文件下载', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_CWS_TUNNEL_DOWN":
            pattern_logs = [{'patterns': ['CAPWAP tunnel to AP %{DATA:apName} went down. Reason: %{DATA:reason}.'],
                             'log_explanation': 'AP下线及下线原因',
                             'log_recommended_action': '·          检查设备AP与设备AC的连接是否正常\n·          检查AP上的配置\n·          检查AC上的配置'}]

        elif log_type_desc == "APMGR_CWS_TUNNEL_UP":
            pattern_logs = [{'patterns': ['%{DATA:tunnelType} CAPWAP tunnel to AP %{DATA:apName} went up.'],
                             'log_explanation': 'AC端配置的AP成功上线，即此AP进入Run状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "APMGR_LOCAL_AC_OFFLINE":
            pattern_logs = [{'patterns': ['Local AC %{DATA:nameLocalAc} went offline. State changed to Idle.'],
                             'log_explanation': 'Local AC下线，状态变为Idle状态',
                             'log_recommended_action': '·          若Local AC主动下线，则不用排查问题\n·          若Local AC异常下线，需要根据调试信息定位并解决问题'}]

        elif log_type_desc == "APMGR_LOCAL_AC_ONLINE":
            pattern_logs = [{'patterns': ['Local AC %{DATA:nameLocalAc} went online. State changed to Run.'],
                             'log_explanation': 'Local AC上线，状态变为运行状态', 'log_recommended_action': '无'}]


    elif module == "STAMGR":

        if log_type_desc == "STAMGR_ADDBAC_INFO":
            pattern_logs = [
                {'patterns': ['Add BAS AC %{DATA:macAddressBasAc}.'], 'log_explanation': 'Master AC与BAS AC建立连接',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_DELBAC_INFO":
            pattern_logs = [
                {'patterns': ['Delete BAS AC %{DATA:macAddressBasAc}.'], 'log_explanation': 'Master AC断开与BAS AC的连接',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_ADD_FAILVLAN":
            pattern_logs = [{'patterns': ['Added a user to the Fail VLAN %{DATA:idFailVlan}.'],
                             'log_explanation': '用户认证失败加入Fail-VLAN', 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_ADDSTA_INFO":
            pattern_logs = [{'patterns': ['Add client %{DATA:macAddressClient}.'], 'log_explanation': '客户端成功连接到BAS AC',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_AUTHORACL_FAILURE":
            pattern_logs = [
                {'patterns': ['Failed to assign an ACL. Reason: %{DATA:param2}.'], 'log_explanation': '下发ACL失败',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_AUTHORUSERPROFILE_FAILURE":
            pattern_logs = [{'patterns': ['Failed to assign a user profile'], 'log_explanation': '下发user profile失败',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_CLIENT_OFFLINE":
            pattern_logs = [{'patterns': [
                'Client %{DATA:macAddressClient} went offline from BSS %{DATA:bssid} with %{DATA:ssidDefinedServiceTemplate}. State changed to Unauth.'],
                             'log_explanation': '客户端在BSS下线，状态变为未认证状态',
                             'log_recommended_action': '·          若客户端主动下线，则不用排查问题\n·          若客户端异常下线，需要查看AP和Radio是否处于正常工作状态，若有异常根据调试信息定位并解决问题'}]

        elif log_type_desc == "STAMGR_CLIENT_ONLINE":
            pattern_logs = [{'patterns': [
                'Client %{DATA:macAddressClient} went online from BSS %{DATA:bssid} with SSID %{DATA:ssidDefinedServiceTemplate}. State changed to Run.'],
                             'log_explanation': '客户端在BSS上线，状态变为运行状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_DELSTA_INFO":
            pattern_logs = [
                {'patterns': ['Delete client %{DATA:macAddressClient}.'], 'log_explanation': '客户端断开与BAS AC的连接',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_DOT1X_LOGIN_FAILURE":
            pattern_logs = [{'patterns': ['A user failed 802.1X authentication.'],
                             'log_explanation': '用户802.1X认证失败。触发该日志的原因可能有：AAA服务器不可用、用户名或密码设置不正确',
                             'log_recommended_action': '·          检查设备与AAA服务器的网络连接是否正常\n·          检查AAA服务器是否正常工作\n·          检查用户名和密码设置是否和AAA服务器上的设置一致'}]

        elif log_type_desc == "STAMGR_DOT1X_LOGIN_SUCC":
            pattern_logs = [{'patterns': ['A user passed 802.1X authentication and came online.'],
                             'log_explanation': '用户通过802.1X认证', 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_DOT1X_LOGOFF":
            pattern_logs = [{'patterns': [
                'Username=%{DATA:username}-UserMAC=%{DATA:macAddressClient}-SSID=%{DATA:ssid}-VLANID=%{DATA:vlanId}; Session for an 802.1X user was terminated.'],
                             'log_explanation': '802.1X用户下线', 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_MACA_LOGIN_FAILURE":
            pattern_logs = [{'patterns': ['A user failed MAC authentication.'],
                             'log_explanation': '用户MAC地址认证失败。触发该日志的原因可能有：AAA服务器不可用、用户名或密码设置不正确',
                             'log_recommended_action': '·          检查设备与AAA服务器的网络连接是否正常\n·          检查AAA服务器是否正常工作\n·          检查用户名和密码设置是否和AAA服务器上的设置一致'}]

        elif log_type_desc == "STAMGR_MACA_LOGIN_SUCC":
            pattern_logs = [
                {'patterns': ['A user passed MAC authentication and came online.'], 'log_explanation': '用户通过MAC地址认证',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_MACA_LOGOFF":
            pattern_logs = [
                {'patterns': ['Session for a MAC authentication user was terminated.'], 'log_explanation': '用户下线',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_STAIPCHANGE_INFO":
            pattern_logs = [
                {'patterns': ['IP address of client %{DATA:macAddressClient} changed to %{DATA:newIpAddressClient}.'],
                 'log_explanation': '客户端更新IP地址', 'log_recommended_action': '无'}]

        elif log_type_desc == "STAMGR_TRIGGER_IP":
            pattern_logs = [{'patterns': ['Intrusion protection triggered. Action: %{DATA:action}.'],
                             'log_explanation': '触发入侵检测，并显示入侵检测模式', 'log_recommended_action': '无'}]


    elif module == "ARP":

        if log_type_desc == "ARP_ACTIVE_ACK_NO_REPLY":
            pattern_logs = [
                {'patterns': ['No ARP reply from IP %{DATA:param0} was received on interface %{DATA:param1}.'],
                 'log_explanation': 'ARP主动确认功能检测到攻击\n接口向所收到ARP报文的发送端IP发送ARP请求，未收到ARP应答',
                 'log_recommended_action': '1.      检查设备上学习到的ARP表项中的IP和MAC是否对应（如果网络部署中存在网关和服务器，优先检查网关和服务器的IP和MAC是否对应）\n2.      请联系技术支持'}]

        elif log_type_desc == "ARP_ACTIVE_ACK_NOREQUESTED_REPLY":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:interfaceName} received from IP %{DATA:ipAddress} an ARP reply that was not requested by the device.'],
                             'log_explanation': 'ARP主动确认功能检测到攻击\n接口在未向ARP报文发送端IP地址发送ARP请求的情况下，收到ARP应答',
                             'log_recommended_action': '设备丢弃该ARP应答'}]

        elif log_type_desc == "ARP_BINDRULETOHW_FAILED":
            pattern_logs = [{'patterns': [
                'Failed to download binding rule to hardware on the interface %{DATA:param0}, SrcIP %{IP:param1}, SrcMAC %{MAC:param2}, VLAN %{NUMBER:param3:int}, Gateway MAC %{MAC:param4}.'],
                             'log_explanation': '由于硬件资源不足、内存不足或其他硬件错误导致绑定规则下发失败',
                             'log_recommended_action': '1.      使用display qos-acl resource查看硬件ACL资源是否充足\n如果充足，则请执行步骤2\n如果不充足，则请取消部分ACL配置或接受当前结果\n2.      使用display memory查看内存资源是否充足\n如果充足，则请执行步骤3\n如果不充足，则请取消部分配置或接受当前结果\n3.      硬件发生错误，请取消最后一次相关配置，并重新尝试'}]

        elif log_type_desc == "ARP_INSPECTION":
            pattern_logs = [{'patterns': [
                'Detected an ARP attack on interface %{DATA:interfaceName}: IP %{DATA:ipAddress}, MAC %{DATA:macAddress}, VLAN %{DATA:vlanId}. %{NUMBER:numberDroppedPackets:int} packet\\(s\\) dropped.'],
                             'log_explanation': 'ARP Detection发现接口下连接的用户发起的攻击，并丢弃了该用户发送的报文',
                             'log_recommended_action': '检查攻击来源'}]

        elif log_type_desc == "ARP_DUPLICATE_IPADDR_DETECT":
            pattern_logs = [{'patterns': [
                'Detected an IP address conflict. The device with MAC address %{DATA:param0} connected to interface %{DATA:param1} in VSI %{DATA:param2} and the device with MAC address %{DATA:param3} connected to interface %{DATA:param4} in VSI %{DATA:param5} were using the same IP address %{IP:param6}.'],
                             'log_explanation': 'ARP检测到重复地址\n接口收到ARP报文中发送端的IP地址，与本设备学习到的ARP表项中的IP地址冲突',
                             'log_recommended_action': '修改IP地址'}]

        elif log_type_desc == "ARP_DYNAMIC":
            pattern_logs = [{'patterns': ['The maximum number of dynamic ARP entries for the device reached.'],
                             'log_explanation': '设备学到的ARP表项总数到达最大值', 'log_recommended_action': '不需处理'}]

        elif log_type_desc == "ARP_DYNAMIC_IF":
            pattern_logs = [
                {'patterns': ['The maximum number of dynamic ARP entries for interface %{DATA:interfaceName} reached.'],
                 'log_explanation': '接口学到的ARP表项总数到达最大值', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "ARP_DYNAMIC_SLOT":
            pattern_logs = [{'patterns': [
                'The maximum number of dynamic ARP entries for slot %{NUMBER:slotNumber:int} reached.',
                'The maximum number of dynamic ARP entries for chassis %{NUMBER:chassisNumber:int} slot %{NUMBER:slotNumber:int} reached.'],
                             'log_explanation': '形式一：\n指定slot学到的动态ARP表项数达到最大值\n形式二：\n指定chassis内slot上学到的动态ARP表项数达到最大值',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "ARP_ENTRY_CONFLICT":
            pattern_logs = [{'patterns': [
                'The software entry for %{DATA:ipAddress} on %{DATA:vpnInstanceName} and the hardware entry did not have the same %{DATA:inconsistentItems}.'],
                             'log_explanation': 'ARP软件表项与硬件表项不一致，比如ARP表项的出接口',
                             'log_recommended_action': '不需要处理，ARP会主动重刷硬件表项'}]

        elif log_type_desc == "ARP_HOST_IP_CONFLICT":
            pattern_logs = [{'patterns': [
                'The host %{DATA:ipAddress} connected to interface %{DATA:interfaceName} cannot communicate correctly, because it uses the same IP address as the host connected to interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口收到主机ARP报文中的源IP与其他接口连接的主机的IP地址冲突',
                             'log_recommended_action': '检查发送ARP报文的主机的合法性。如果非法，需要断开该主机网络'}]

        elif log_type_desc == "ARP_LOCALPROXY_ENABLE_FAILED":
            pattern_logs = [{'patterns': ['Failed to enable local proxy ARP on interface %{DATA:interfaceName}.'],
                             'log_explanation': 'VSI虚接口下开启ARP本地代理失败。主控板设置成功、非主控板设置失败的情况下在相应非主控板打印',
                             'log_recommended_action': '1.      检查设备相应单板是否支持本功能；\n2.      确认设备的硬件资源是否充足'}]

        elif log_type_desc == "ARP_RATE_EXCEEDED":
            pattern_logs = [{'patterns': [
                'The ARP packet rate \\(%{NUMBER:param0:int} pps\\) exceeded the rate limit \\(%{NUMBER:param1:int} pps\\) on interface %{DATA:param2} in the last %{NUMBER:param3:int} seconds.'],
                             'log_explanation': '接口接收ARP报文速率超过了接口的限速值', 'log_recommended_action': '检查ARP报文发送主机的合法性'}]

        elif log_type_desc == "ARP_RATELIMIT_NOTSUPPORT":
            pattern_logs = [{'patterns': ['ARP packet rate limit is not support on slot %{NUMBER:slotNumber:int}.',
                                          'ARP packet rate limit is not support on chassis %{NUMBER:chassisNumber:int} slot %{NUMBER:slotNumber:int}.'],
                             'log_explanation': '形式一：\n指定slot不支持ARP报文限速功能\n形式二：\n指定chassis内slot不支持ARP报文限速功能',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "ARP_SENDER_IP_INVALID":
            pattern_logs = [{'patterns': [
                'Sender IP %{DATA:ipAddress} was not on the same network as the receiving interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口收到ARP报文中发送端IP与本接口不在同一网段',
                             'log_recommended_action': '检查发送端IP对应主机的合法性'}]

        elif log_type_desc == "ARP_SENDER_MAC_INVALID":
            pattern_logs = [{'patterns': [
                'Sender MAC %{DATA:macAddress} was not identical to Ethernet source MAC %{DATA:macAddress} on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口收到ARP报文的以太网数据帧首部中的源MAC地址和ARP报文中的发送端MAC地址不同',
                             'log_recommended_action': '检查发送端MAC地址对应主机的合法性'}]

        elif log_type_desc == " ARP_SENDER_SMACCONFLICT":
            pattern_logs = [{'patterns': [
                'Packet was discarded because its sender MAC address was the MAC address of the receiving interface.\nInterface: %{DATA:interfaceName}, sender IP: %{DATA:senderIpAddress}, target IP: %{DATA:targetIpAddress}.'],
                             'log_explanation': '设备从接口GigabitEthernet1/0/1接收到的ARP报文中的源MAC和设备的MAC地址冲突',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == " ARP_SENDER_SMACCONFLICT_VSI":
            pattern_logs = [{'patterns': [
                'Packet was discarded because its sender MAC address was the MAC address of the receiving interface.\nInterface: %{DATA:interfaceName}, sender IP: %{DATA:senderIpAddress}, target IP: %{DATA:targetIpAddress},VSI index: %{NUMBER:vsiIndex:int}, link ID: %{NUMBER:linkId:int}.'],
                             'log_explanation': '设备从VSI接口3接收到的ARP报文中的源MAC和设备的MAC地址冲突',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "ARP_SRC_MAC_FOUND_ATTACK":
            pattern_logs = [
                {'patterns': ['An attack from MAC %{DATA:macAddress} was detected on interface %{DATA:interfaceName}.'],
                 'log_explanation': '源MAC地址固定的ARP攻击检测功能检测到攻击\n5秒内，收到同一源MAC地址（源MAC地址固定）的ARP报文超过一定的阈值',
                 'log_recommended_action': '检查该源MAC地址对应主机的合法性'}]

        elif log_type_desc == "ARP_SUP_ENABLE_FAILED":
            pattern_logs = [{'patterns': ['Failed to enable ARP flood suppression on VSI %{DATA:vsiName}.'],
                             'log_explanation': '在VSI内开启ARP泛洪抑制功能失败。本日志打印间隔时间为不低于2s，若配置下发过快，部分日志信息将不能输出',
                             'log_recommended_action': '3.      检查设备是否支持本功能；\n4.      确认设备的硬件资源是否足够'}]

        elif log_type_desc == "ARP_TARGET_IP_INVALID":
            pattern_logs = [{'patterns': [
                'Target IP %{DATA:ipAddress} was not the IP of the receiving interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口收到ARP报文中的目标IP与本接口IP不一致',
                             'log_recommended_action': '检查发送ARP报文的主机的合法性'}]

        elif log_type_desc == "ARP_THRESHOLD_REACHED":
            pattern_logs = [{'patterns': [
                'The alarm threshold for dynamic ARP entry learning was reached on interface %{DATA:param0}.'],
                             'log_explanation': '接口GigabitEthernet1/0/1学习的动态ARP表项个数到达了告警门限值',
                             'log_recommended_action': '检查该接口学习这么多ARP表项是否合理，网络内是否存在攻击源'}]

        elif log_type_desc == "ARP_USER_DUPLICATE_IPADDR_DETECT":
            pattern_logs = [{'patterns': [
                'Detected a user IP address conflict. New user \\(MAC %{DATA:macAddressNewUser}, SVLAN %{DATA:outerVlanNewUserBelongs}, CVLAN %{DATA:innerVlanNewUserBelongs}\\) on interface %{DATA:nameInterfaceConnectingNewUser} and old user \\(MAC %{DATA:macAddressOldUser}, SVLAN %{DATA:outerVlanOldUserBelongs}, CVLAN %{DATA:innerVlanOldUserBelongs}\\) on interface %{DATA:nameInterfaceConnectingOldUser} were using the same IP address %{IP:ipAddress}.'],
                             'log_explanation': 'ARP检测到终端用户间IP地址冲突，某个新用户的IP地址和某个旧用户的IP地址冲突',
                             'log_recommended_action': '排查所有终端用户的IP地址，解决IP地址冲突问题'}]

        elif log_type_desc == "ARP_USER_MOVE_DETECT":
            pattern_logs = [{'patterns': [
                'Detected a user \\(IP address %{IP:ipAddressUser}, MAC address %{DATA:macAddressUser}\\) moved to another interface. Before user move: interface %{DATA:interfaceNameMigration}, SVLAN %{DATA:outerVlanUserBelongsMigration}, CVLAN %{DATA:innerVlanUserBelongsMigration}. After user move: interface %{DATA:interfaceNameMigration}, SVLAN %{DATA:outerVlanUserBelongsMigration}, CVLAN %{DATA:innerVlanUserBelongsMigration}.'],
                             'log_explanation': 'ARP检测到终端用户发生接口迁移动作',
                             'log_recommended_action': '使用display arp user-move record命令查看终端用户迁移信息，检查迁移是否合理'}]

        elif log_type_desc == "DUPIFIP":
            pattern_logs = [{'patterns': [
                'Duplicate address %{DATA:ipAddress} on interface %{DATA:interfaceName}, sourced from %{DATA:macAddress}.'],
                             'log_explanation': 'ARP检测到重复地址\n接口收到ARP报文的发送端IP地址与该接口的IP地址重复',
                             'log_recommended_action': '修改IP地址配置'}]

        elif log_type_desc == "DUPIP":
            pattern_logs = [{'patterns': [
                'IP address %{DATA:ipAddress} conflicted with global or imported IP address, sourced from %{DATA:macAddress}.'],
                             'log_explanation': '收到ARP报文中的发送端IP地址与全局或导入的IP地址冲突', 'log_recommended_action': '修改IP地址配置'}]

        elif log_type_desc == "DUPVRRPIP":
            pattern_logs = [{'patterns': [
                'IP address %{DATA:ipAddress} conflicted with VRRP virtual IP address on interface %{DATA:interfaceName}, sourced from %{DATA:macAddress}.'],
                             'log_explanation': '收到ARP报文中的发送端IP与VRRP虚拟IP地址冲突', 'log_recommended_action': '修改IP地址配置'}]


    elif module == "ATK":

        if log_type_desc == "ATK_ICMP_UNREACHABLE":
            pattern_logs = [{'patterns': [
                'IcmpType\\(1058\\)=%{NUMBER:icmpMessageType:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，ICMP目的不可达的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMP_UNREACHABLE_RAW":
            pattern_logs = [{'patterns': [
                'IcmpType\\(1058\\)=%{NUMBER:icmpMessageType:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMP目的不可达的报文首包触发日志；日志聚合开关关闭，每个ICMP目的不可达的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMP_UNREACHABLE_RAW_SZ":
            pattern_logs = [{'patterns': [
                'IcmpType\\(1058\\)=%{NUMBER:icmpMessageType:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMP目的不可达的报文首包触发日志；日志聚合开关关闭，每个ICMP目的不可达的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMP_UNREACHABLE_SZ":
            pattern_logs = [{'patterns': [
                'IcmpType\\(1058\\)=%{NUMBER:icmpMessageType:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，ICMP目的不可达的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMP_ECHO_REQ_RAW":
            pattern_logs = [{'patterns': [
                'IcmpType\\(1058\\)=%{NUMBER:icmpMessageType:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; DstPort\\(1004\\)=%{NUMBER:destinationPortNumber:int}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMP请求回显报文首包触发日志；日志聚合开关关闭，每个ICMP请求回显报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMP_ECHO_REQ_RAW_SZ":
            pattern_logs = [{'patterns': [
                'IcmpType\\(1058\\)=%{NUMBER:icmpMessageType:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; DstPort\\(1004\\)=%{NUMBER:destinationPortNumber:int}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMP请求回显报文首包触发日志；日志聚合开关关闭，每个ICMP请求回显报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_UDP_FLOOD":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; UpperLimit\\(1048\\)=%{NUMBER:rateLimit:int}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '单位时间内指定IPV4目的地址的UDP报文数超过阈值，触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_UDP_FLOOD_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; UpperLimit\\(1048\\)=%{NUMBER:rateLimit:int}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '单位时间内指定IPV4目的地址的UDP报文数超过阈值，触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_UDP_SNORK":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，IPV4源端口为7、19或135，目的端口为135的UDP报文数超过1，聚合后触发日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_UDP_SNORK_RAW":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，IPV4源端口为7、19或135，目的端口为135的UDP报文首包触发日志；日志聚合开关关闭，每个IPV4源端口为7、19或135，目的端口为135的UDP报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_UDP_SNORK_RAW_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，IPV4源端口为7、19或135，目的端口为135的UDP报文首包触发日志；日志聚合开关关闭，每个IPV4源端口为7、19或135，目的端口为135的UDP报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_UDP_SNORK_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，IPV4源端口为7、19或135，目的端口为135的UDP报文数超过1，聚合后触发日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMPV6_TYPE":
            pattern_logs = [{'patterns': [
                'Icmpv6Type\\(1059\\)=%{NUMBER:icmpv6MessageType:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，ICMPV6用户自定义类型的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMPV6_TYPE_RAW":
            pattern_logs = [{'patterns': [
                'Icmpv6Type\\(1059\\)=%{NUMBER:icmpv6MessageType:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMPV6用户自定义类型的报文首包触发日志；日志聚合开关关闭，每个ICMPV6用户自定义类型的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMPV6_TYPE_RAW_SZ":
            pattern_logs = [{'patterns': [
                'Icmpv6Type\\(1059\\)=%{NUMBER:icmpv6MessageType:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMPV6用户自定义类型的报文首包触发日志；日志聚合开关关闭，每个ICMPV6用户自定义类型的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMPV6_TYPE_SZ":
            pattern_logs = [{'patterns': [
                'Icmpv6Type\\(1059\\)=%{NUMBER:icmpv6MessageType:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，ICMPV6用户自定义类型的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_UDP_FLOOD":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; UpperLimit\\(1048\\)=%{NUMBER:rateLimit:int}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '单位时间内指定IPV6目的地址的UDP报文数超过阈值，触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_UDP_FLOOD_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; UpperLimit\\(1048\\)=%{NUMBER:rateLimit:int}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '单位时间内指定IPV6目的地址的UDP报文数超过阈值，触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_UDP_SNORK":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，IPV6源端口为7、19或135，目的端口为135的UDP报文数超过1，聚合后触发日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_UDP_SNORK_RAW":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，IPV6源端口为7、19或135，目的端口为135的UDP报文首包触发日志；日志聚合开关关闭，每个IPV6源端口为7、19或135，目的端口为135的UDP报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_UDP_SNORK_RAW_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，IPV6源端口为7、19或135，目的端口为135的UDP报文首包触发日志；日志聚合开关关闭，每个IPV6源端口为7、19或135，目的端口为135的UDP报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_UDP_SNORK_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，IPV6源端口为7、19或135，目的端口为135的UDP报文数超过1，聚合后触发日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMPV6_TRACEROUTE_RAW":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMP类型为3的报文首包触发日志；日志聚合开关关闭，每个ICMP类型为3的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_ICMPV6_TRACEROUTE_RAW_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}.'],
                             'log_explanation': '日志聚合开关开启，ICMP类型为3的报文首包触发日志；日志聚合开关关闭，每个ICMP类型为3的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_TIMESTAMP":
            pattern_logs = [{'patterns': [
                'IPOptValue\\(1057\\)=%{NUMBER:ipOptionValue:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，IP选项为68的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_TIMESTAMP_RAW":
            pattern_logs = [{'patterns': [
                'IPOptValue\\(1057\\)=%{NUMBER:ipOptionValue:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，IP选项为68的报文首包触发日志；日志聚合开关关闭，每个IP选项为68的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_TIMESTAMP_RAW_SZ":
            pattern_logs = [{'patterns': [
                'IPOptValue\\(1057\\)=%{NUMBER:ipOptionValue:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，IP选项为68的报文首包触发日志；日志聚合开关关闭，每个IP选项为68的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_TIMESTAMP_SZ":
            pattern_logs = [{'patterns': [
                'IPOptValue\\(1057\\)=%{NUMBER:ipOptionValue:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，IP选项为68的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_DIS_PORTSCAN":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; Protocol\\(1001\\)=%{DATA:protocolName}; TcpFlag\\(1074\\)=%{DATA:tcpPacketType}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '报文满足分布式port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_DIS_PORTSCAN_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; Protocol\\(1001\\)=%{DATA:protocolName}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '报文满足分布式port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_ABNORMAL":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，两个以上IP选项置位的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_ABNORMAL_RAW":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，两个以上IP选项置位的报文首包触发日志；日志聚合开关关闭，每个两个以上IP选项置位的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_ABNORMAL_RAW_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，两个以上IP选项置位的报文首包触发日志；日志聚合开关关闭，每个两个以上IP选项置位的报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_ABNORMAL_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，两个以上IP选项置位的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_IPSWEEP":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '报文满足ip sweep时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_IPSWEEP_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '报文满足ip sweep时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_PORTSCAN":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '报文满足port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_PORTSCAN_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '报文满足port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP4_SYN_FLOOD_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; UpperLimit\\(1048\\)=%{NUMBER:rateLimit:int}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': '单位时间内指定目的地址的TCP标志位为SYN的IPV4报文数超过阈值，触发日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_DIS_PORTSCAN":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; Protocol\\(1001\\)=%{DATA:protocolName}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': 'IPV6报文满足分布式port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_DIS_PORTSCAN_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; Protocol\\(1001\\)=%{DATA:protocolName}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': 'IPV6报文满足分布式port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_IMPOSSIBLE":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，源目的地址相同的IPV6报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_IMPOSSIBLE_RAW":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，源目的地址相同的IPV4报文首包触发日志；日志聚合开关关闭，每个源目的地址相同的IPV4报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_IMPOSSIBLE_RAW_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，源目的地址相同的IPV4报文首包触发日志；日志聚合开关关闭，每个源目的地址相同的IPV4报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_IMPOSSIBLE_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关开启，源目的地址相同的IPV6报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_IPSWEEP":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': 'IPV6报文满足ip sweep时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_IPSWEEP_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': 'IPV6报文满足ip sweep时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_PORTSCAN":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:param0}; Protocol\\(1001\\)=%{DATA:param1}; SrcIPv6Addr\\(1036\\)=%{IP:param2}; RcvVPNInstance\\(1041\\)=%{DATA:param3}; DstIPv6Addr\\(1037\\)=%{IP:param4}; Action\\(1049\\)=%{DATA:param5}; BeginTime_c\\(1011\\)=%{DATA:param6}.'],
                             'log_explanation': 'IPV6报文满足port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IP6_PORTSCAN_SZ":
            pattern_logs = [{'patterns': [
                'SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; Protocol\\(1001\\)=%{DATA:protocolName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}.'],
                             'log_explanation': 'IPV6报文满足port scan时触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_LOOSESRCROUTE":
            pattern_logs = [{'patterns': [
                'IPOptValue\\(1057\\)=%{NUMBER:ipOptionValue:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)= %{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，IP选项为131的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPOPT_LOOSESRCROUTE_SZ":
            pattern_logs = [{'patterns': [
                'IPOptValue\\(1057\\)=%{NUMBER:ipOptionValue:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:ipAddressPeerDs-liteTunnelInterface}; DstIPAddr\\(1007\\)=%{IP:destinationIpAddress}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Protocol\\(1001\\)=%{DATA:protocolType}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)= %{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，IP选项为131的报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPV6_EXT_HEADER":
            pattern_logs = [{'patterns': [
                'IPv6ExtHeader\\(1060\\)=%{NUMBER:ipv6ExtensionHeaderValue:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，自定义扩展头的IPV6报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPV6_EXT_HEADER_RAW":
            pattern_logs = [{'patterns': [
                'IPv6ExtHeader\\(1060\\)=%{NUMBER:ipv6ExtensionHeaderValue:int}; RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，自定义扩展头的IPV6报文首包触发日志；日志聚合开关关闭，每个自定义扩展头的IPV6报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPV6_EXT_HEADER_RAW_SZ":
            pattern_logs = [{'patterns': [
                'IPv6ExtHeader\\(1060\\)=%{NUMBER:ipv6ExtensionHeaderValue:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}.'],
                             'log_explanation': '日志聚合开关开启，自定义扩展头的IPV6报文首包触发日志；日志聚合开关关闭，每个自定义扩展头的IPV6报文触发一个日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ATK_IPV6_EXT_HEADER_SZ":
            pattern_logs = [{'patterns': [
                'IPv6ExtHeader\\(1060\\)=%{NUMBER:ipv6ExtensionHeaderValue:int}; SrcZoneName\\(1025\\)=%{DATA:sourceSecurityZoneName}; SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address}; DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:nameReceivingVpnInstance}; Action\\(1049\\)=%{DATA:actionsAttack}; BeginTime_c\\(1011\\)=%{DATA:startTimeAttack}; EndTime_c\\(1012\\)=%{DATA:endTimeAttack}; AtkTimes\\(1050\\)=%{NUMBER:attackTimes:int}.'],
                             'log_explanation': '日志聚合开关打开，自定义扩展头的IPV6报文数超过1，聚合后触发日志', 'log_recommended_action': '无'}]


    elif module == "ATM":

        if log_type_desc == "ATM_PVCDOWN":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:nameInterfacePvcBelongs} PVC %{NUMBER:vpiValuePvc:int}/%{NUMBER:vciValuePvc:int} status is down.'],
                             'log_explanation': 'PVC的状态转变为down。触发该日志的原因可能有：PVC所属ATM接口状态转变为down、PVC的OAM状态转变为down或该PVC被shutdown',
                             'log_recommended_action': '1.      使用display atm pvc-info命令查看指定接口的PVC详细信息，根据显示信息进行如下处理：\n2.      如果Interface State字段显示为DOWN\n·          使用display interface atm命令分别检查本端和对端的ATM接口是否被手动shutdown，若是，可通过在接口上执行undo shutdown命令解决该问题\n·          检查接口之间的连线是否插好\n3.      如果OAM State字段显示为DOWN\n·          当两台路由器直连时：\n¡  检查对端接口上创建的PVC的VPI/VCI是否与本端相同\n¡  检查对端接口上PVC的OAM配置是否与本端一致（比如本端配置了oam cc sink，对端需配置oam cc source）\n¡  检查对端的PVC是否被手动shutdown，若是，可通过在PVC视图上执行undo shutdown命令解决该问题\n¡  检查两端连线是否正确\n·          当两台路由器通过ATM交换网络连接时，除检查上述几点外，还需要检查交换网络中转发规则配置是否正确，如果两端PVC在交换网络中不可达，PVC状态同样为down\n4.      如果PVC State字段显示为DOWN，请检查本端的PVC是否被手动shutdown，若是，可通过在PVC视图上执行undo shutdown命令解决该问题'}]

        elif log_type_desc == "ATM_PVCUP":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:nameInterfacePvcBelongs} PVC %{NUMBER:vpiValuePvc:int}/%{NUMBER:vciValuePvc:int} status is up.'],
                             'log_explanation': 'PVC的状态转变为up', 'log_recommended_action': '1.      无需处理'}]


    elif module == "BFD":

        if log_type_desc == "BFD_CHANGE_FSM":
            pattern_logs = [{'patterns': [
                'Sess%{DATA:sourceAddress}, Ver, Sta: %{DATA:nameFsmChanging}->%{DATA:nameFsmChanging}, Diag: %{DATA:diagnosticInformation}'],
                             'log_explanation': 'BFD会话的状态机发生变化。当BFD会话up或down时出现此信息。如果出现会话异常丢失的情况，可能由高错误率或高丢包率导致',
                             'log_recommended_action': '需要检查是否BFD配置的问题或网络出现拥塞'}]

        elif log_type_desc == "BFD_REACHED_UPPER_LIMIT":
            pattern_logs = [{'patterns': [
                'The total number of BFD sessions %{NUMBER:totalNumberBfdSessions:int} reached the upper limit. Can’t create a new session.'],
                             'log_explanation': 'BFD会话总数达到上限', 'log_recommended_action': '请检查BFD会话配置'}]


    elif module == "BGP":

        if log_type_desc == "BGP_EXCEED_ROUTE_LIMIT":
            pattern_logs = [{'patterns': [
                'BGP.%{DATA:vpnInstanceName}: The number of routes from peer %{DATA:ipAddressBgpPeer} \\(%{DATA:addressFamilyBgpPeer}\\) exceeds the limit %{NUMBER:maximumNumberRoutes:int}.'],
                             'log_explanation': '从对等体学到的路由数量超过了允许的最大路由数量',
                             'log_recommended_action': '检查是否是攻击导致，如果是，需要管理员找到问题原因，对攻击进行防御\n否则，查看是否需要增大允许的最大路由数量'}]

        elif log_type_desc == "BGP_REACHED_THRESHOLD":
            pattern_logs = [{'patterns': [
                'BGP.%{DATA:vpnInstanceName}: The ratio of the number of routes received from peer %{DATA:ipAddressBgpPeer} \\(%{DATA:addressFamilyBgpPeer}\\) to the number of allowed routes %{NUMBER:maximumNumberRoutesReceivedBgpPeer:int} has reached the threshold \\(%{NUMBER:percentageReceivedRoutesMaximumAllowedRoutes:int}%\\).'],
                             'log_explanation': '接收的路由数量占允许的最大路由数量的百分比达到了阈值',
                             'log_recommended_action': '检查是否是攻击导致，如果是，需要管理员找到问题原因，对攻击进行防御\n否则，查看是否需要增大以下数值：\n·          允许的最大路由数量\n·          接收的路由数量占允许的最大路由数量百分比的阈值'}]

        elif log_type_desc == "BGP_LOG_ROUTE_FLAP":
            pattern_logs = [{'patterns': [
                'BGP.%{DATA:vpnInstanceName}: The route %{DATA:rdBgpRoute} %{DATA:bgpRoutePrefix}/%{NUMBER:maskBgpRoutePrefix:int} learned from peer %{DATA:ipAddressBgpPeer} \\(%{DATA:addressFamilyBgpPeer}\\) flapped.'],
                             'log_explanation': '从对等体学到的路由发生抖动',
                             'log_recommended_action': '检查路由抖动是否不正常，如果是，需要管理员找到路由抖动的源头，并制定解决方案'}]

        elif log_type_desc == "BGP_MEM_ALERT":
            pattern_logs = [{'patterns': ['BGP process received system memory alert %{DATA:typeMemoryAlarm} event.'],
                             'log_explanation': 'BGP模块收到内存告警信息',
                             'log_recommended_action': '如果内存告警类型为start，请检查系统内存占用情况，对占用内存较多的模块进行调整，尽量释放可用内存'}]

        elif log_type_desc == "BGP_PEER_LICENSE_REACHED":
            pattern_logs = [{'patterns': ['Number of peers in Established state reached the license limit.'],
                             'log_explanation': '处于established状态的邻居数量已达到license规格限制',
                             'log_recommended_action': '检查license安装情况，判断是否需要安装新的license'}]

        elif log_type_desc == "BGP_ROUTE_LICENSE_REACHED":
            pattern_logs = [{'patterns': ['Number of %{DATA:bgpAddressFamily} routes reached the license limit.'],
                             'log_explanation': '指定类型的路由数量已达到license规格限制',
                             'log_recommended_action': '检查license安装情况，判断是否需要安装新的license\n当指定类型的路由数量降低到License的规格限制以下或者License规格限制扩大时，之前被丢弃的路由不能自动恢复，需要用户手工配置，以便重新学习路由'}]

        elif log_type_desc == "BGP_STATE_CHANGED":
            pattern_logs = [{'patterns': [
                'BGP.%{DATA:param0}: %{DATA:param1} state has changed from %{DATA:param2} to %{DATA:param3}.'],
                             'log_explanation': 'BGP对等体的状态发生变化\n此日志信息当BGP对等体从其他状态进入Established状态或者从Established状态进入其他状态时产生',
                             'log_recommended_action': '如果BGP对等体意外Down，请检查网络是否发生故障或丢包'}]

        elif log_type_desc == "BGP_STATE_CHANGED_REASON":
            pattern_logs = [{'patterns': [
                'BGP.%{DATA:vpnInstanceName}: %{DATA:ipAddressBgpPeer} state has changed from %{DATA:originalBgpPeerState} to %{DATA:newBgpPeerState}. \\(%{DATA:bgpPeerInformation}\\)'],
                             'log_explanation': '当BGP对等体从Established状态进入其他状态时打印提示信息',
                             'log_recommended_action': '请根据会话断开的原因检查网络是否发生故障或丢包'}]


    elif module == "BLS":

        if log_type_desc == "BLS_ENTRY_ADD":
            pattern_logs = [{'patterns': [
                'SrcIPAddr\\(1003\\)=%{IP:blacklistedIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:peerAddressDs-liteTunnel}; RcvVPNInstance\\(1041\\)=%{DATA:vpnInstanceName}; TTL\\(1051\\)=%{DATA:ttlBlacklistEntry}; Reason\\(1052\\)=%{DATA:reasonBlacklistEntryAdded}.'],
                             'log_explanation': '日志开关打开；手动配置一个黑名单；scan检测添加一个黑名单；触发日志发送', 'log_recommended_action': '无'}]

        elif log_type_desc == "BLS_ENTRY_DEL":
            pattern_logs = [{'patterns': [
                'SrcIPAddr\\(1003\\)=%{IP:blacklistedIpAddress}; DSLiteTunnelPeer\\(1040\\)=%{DATA:peerAddressDs-liteTunnel}; RcvVPNInstance\\(1041\\)=%{DATA:vpnInstanceName}; Reason\\(1052\\)=%{DATA:reasonBlacklistEntryDeleted}.'],
                             'log_explanation': '日志开关打开；手动删除一个黑名单；老化删除一个黑名单；触发日志发送', 'log_recommended_action': '无'}]

        elif log_type_desc == "BLS_IPV6_ENTRY_ADD":
            pattern_logs = [{'patterns': [
                'SrcIPv6Addr\\(1036\\)=%{IP:blacklistedIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:vpnInstanceName}; TTL\\(1051\\)=%{DATA:ttlBlacklistEntry}; Reason\\(1052\\)=%{DATA:reasonBlacklistEntryAdded}.'],
                             'log_explanation': '日志开关打开；手动配置一个黑名单；scan检测添加一个黑名单；触发日志发送', 'log_recommended_action': '无'}]

        elif log_type_desc == "BLS_IPV6_ENTRY_DEL":
            pattern_logs = [{'patterns': [
                'SrcIPv6Addr\\(1036\\)=%{IP:blacklistedIpv6Address}; RcvVPNInstance\\(1041\\)=%{DATA:vpnInstanceName}; Reason\\(1052\\)=%{DATA:reasonBlacklistEntryDeleted}.'],
                             'log_explanation': '日志开关打开；手动删除一个黑名单；老化删除一个黑名单；触发日志发送', 'log_recommended_action': '无'}]


    elif module == "CFD":

        if log_type_desc == "CFD_CROSS_CCM":
            pattern_logs = [{'patterns': [
                'MEP %{NUMBER:serviceInstanceId:int} in SI %{NUMBER:localMepId:int} received a cross-connect CCM. It’s SrcMAC is %{MAC:sourceMacAddress}, SeqNum is %{NUMBER:sequenceNumber:int}, RMEP is %{NUMBER:remoteMepId:int}, MD ID is %{DATA:mdId}, MA ID is %{DATA:maId}.'],
                             'log_explanation': 'MEP收到交叉连接的CCM报文，该报文包含与本端不同的MA ID或MD ID',
                             'log_recommended_action': '检查两端MEP的配置。让MEP所属的MD和MA的配置一致，且两端MEP级别相同、方向都相同'}]

        elif log_type_desc == "CFD_ERROR_CCM":
            pattern_logs = [{'patterns': [
                'MEP %{NUMBER:serviceInstanceId:int} in SI %{NUMBER:localMepId:int} received an error CCM. It’s SrcMAC is %{MAC:sourceMacAddress}, SeqNum is %{NUMBER:sequenceNumber:int}, RMEP is %{NUMBER:remoteMepId:int}, MD ID is %{DATA:mdId}, MA ID is %{DATA:maId}.'],
                             'log_explanation': 'MEP收到错误的CCM报文，该报文包含错误的MEP ID或生存时间',
                             'log_recommended_action': '检查CCM配置。让两端的CC检测周期配置一致，并配置远端MEP ID在本端允许的MEP列表中'}]

        elif log_type_desc == "CFD_LOST_CCM":
            pattern_logs = [{'patterns': [
                'MEP %{NUMBER:localMepId:int} in SI %{NUMBER:serviceInstanceId:int} failed to receive CCMs from RMEP %{NUMBER:remoteMepId:int}.'],
                             'log_explanation': 'MEP在3.5个CCM报文发送周期内没有收到CCM报文，可能的原因是链路故障或远端MEP在此期间没有发送CCM报文',
                             'log_recommended_action': '检查链路状态和远端MEP的配置。如果链路down了或有其它的故障，例如单通故障，则恢复此链路。如果远端配置了同一服务实例的MEP，则确认两端的CC发送周期是一致的'}]

        elif log_type_desc == "CFD_RECEIVE_CCM":
            pattern_logs = [{'patterns': [
                'MEP %{NUMBER:localMepId:int} in SI %{NUMBER:serviceInstanceId:int} received CCMs from RMEP %{NUMBER:remoteMepId:int}'],
                             'log_explanation': 'MEP收到远端MEP发送的CCM报文', 'log_recommended_action': '无'}]


    elif module == "CFGMAN":

        if log_type_desc == "CFGMAN_ARCHIVE_SCP_FAIL":
            pattern_logs = [{'patterns': [
                'Archive configuration to SCP server failed: IP = %{DATA:ipAddressScpServer}, Directory = %{DATA:directorySavesConfigurationArchivesScpServer}, Username = %{DATA:usernameLoggingScpServer}'],
                             'log_explanation': '设备向SCP服务器保存配置文件失败时，打印此日志信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "CFGMAN_CFGCHANGED":
            pattern_logs = [{'patterns': ['Configuration changed.'],
                             'log_explanation': '如果配置在过去的十分钟内发生了变化，设备将记录事件索引、引起配置变化的来源、源配置以及目的配置',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "CFGMAN_EXIT_FROM_CONFIGURE":
            pattern_logs = [{'patterns': [
                'Line=%{DATA:userLineName}, IP address=%{DATA:ipAddressUser}, user=%{DATA:username}; Exit from the system view or a feature view to the user view.'],
                             'log_explanation': '记录交互模式下用户从系统视图、功能视图退出到用户视图', 'log_recommended_action': '无'}]

        elif log_type_desc == "CFGMAN_OPTCOMPLETION":
            pattern_logs = [{'patterns': ['Operation completed.'], 'log_explanation': '操作完成后记录操作的类型、状态以及时间',
                             'log_recommended_action': '请根据OperateState的值定位、处理问题'}]

        elif log_type_desc == "CFG_SAVE_FAILED":
            pattern_logs = [{'patterns': ['Failed to save the current configuration.',
                                          'Failed to save the current configuration on %{DATA:param0}.',
                                          'Failed to save the current configuration. Reason: %{DATA:param1}.',
                                          'Failed to save the current configuration for %{DATA:param2}.',
                                          'Failed to save the current configuration on %{DATA:param3}. Reason: %{DATA:param4}.'],
                             'log_explanation': '保存当前配置失败时输入本日志，其中：\n·          配置保存失败的原因，原因不明确的提示形式一\n·          对于形式二，一般在如下情况下输出：由于磁盘读写慢、磁盘损坏等原因，将配置文件备份到备用主控板失败\n·          不提示板卡表示主用主控板和备用主控板配置保存失败，提示板卡表示指定板卡配置保存失败\n·          MDC/Context内的配置保存失败，具体信息请登录MDC/Context，执行display logbuffer命令查看',
                             'log_recommended_action': '1.      执行dir命令查看主用主控板和备用主控板的磁盘空间是否充足\n2.      执行copy命令检查主用主控板和备用主控板的磁盘是否可以正常Copy文件\n3.      执行display memory和display process memory命令查看内存信息，检查设备内存空间是否充足\n4.      如果没有发现上述问题，请联系技术支持'}]

        elif log_type_desc == "CFG_SET_NEXTCFG_FAILED":
            pattern_logs = [{'patterns': [
                'Failed to set %{DATA:fileName} as the %{DATA:mainBackupAttribute} next-startup file on %{DATA:slotLocationSlotOneCpuCpuLocationSlotMultipleCpus}.'],
                             'log_explanation': '设置下次启动配置文件失败',
                             'log_recommended_action': '请确认文件是否存在，文件内容是否合法。如果没有发现错误，请记录当时操作，联系技术支持'}]


    elif module == "CONNLMT":

        if log_type_desc == "CONNLMT_IPV4_OVERLOAD":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:global};Protocol\\(1001\\)=%{DATA:transportLayerProtocolType};SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress};DstIPAddr\\(1007\\)=%{IP:destinationIpAddress};ServicePort\\(1071\\)=%{NUMBER:servicePortNumber:int};RcvVPNInstance\\(1042\\)=%{DATA:sourceVpnInstanceName};SndVPNInstance\\(1043\\)=%{DATA:destinationVpnInstanceName};SndDSLiteTunnelPeer\\(1041\\)=%{DATA:peerTunnelId};UpperLimit\\(1049\\)=%{NUMBER:upperThreshold:int};LimitRuleNum\\(1051\\)=%{NUMBER:ruleId:int};Event\\(1048\\)=%{DATA:eventMessage};'],
                             'log_explanation': '当连接数的并发数超过策略中配置的上限时触发日志输出', 'log_recommended_action': '无'}]

        elif log_type_desc == "CONNLMT_IPV4_RECOVER":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:global};Protocol\\(1001\\)=%{DATA:transportLayerProtocolType};SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress};DstIPAddr\\(1007\\)=%{IP:destinationIpAddress};ServicePort\\(1071\\)=%{NUMBER:servicePortNumber:int};RcvVPNInstance\\(1042\\)=%{DATA:sourceVpnInstanceName};SndVPNInstance\\(1043\\)=%{DATA:destinationVpnInstanceName};SndDSLiteTunnelPeer\\(1041\\)=%{DATA:peerTunnelId};DropPktCount\\(1052\\)=%{NUMBER:numberDroppedPackets:int};LowerLimit\\(1050\\)=%{NUMBER:lowerThreshold:int};LimitRuleNum\\(1051\\)=%{NUMBER:ruleId:int};Event\\(1048\\)=%{DATA:eventMessage};'],
                             'log_explanation': '当连接数的并发数从达到上限恢复到下限时触发日志输出', 'log_recommended_action': '无'}]

        elif log_type_desc == "CONNLMT_IPV6_OVERLOAD":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:global};Protocol\\(1001\\)=%{DATA:transportLayerProtocolType};SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address};DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address};ServicePort\\(1071\\)=%{NUMBER:servicePortNumber:int};RcvVPNInstance\\(1042\\)=%{DATA:sourceVpnInstanceName};SndVPNInstance\\(1043\\)=%{DATA:destinationVpnInstanceName};SndDSLiteTunnelPeer\\(1041\\)=%{DATA:peerTunnelId};UpperLimit\\(1049\\)=%{NUMBER:upperThreshold:int};LimitRuleNum\\(1051\\)=%{NUMBER:ruleId:int};Event\\(1048\\)=%{DATA:eventMessage};'],
                             'log_explanation': '当连接数的并发数超过策略中配置的上限时触发日志输出', 'log_recommended_action': '无'}]

        elif log_type_desc == "CONNLMT_IPV6_RECOVER":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:global};Protocol\\(1001\\)=%{DATA:transportLayerProtocolType};SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address};DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address};ServicePort\\(1071\\)=%{NUMBER:servicePortNumber:int};RcvVPNInstance\\(1042\\)=%{DATA:sourceVpnInstanceName};SndVPNInstance\\(1043\\)=%{DATA:destinationVpnInstanceName};SndDSLiteTunnelPeer\\(1041\\)=%{DATA:peerTunnelId};DropPktCount\\(1052\\)=%{NUMBER:numberDroppedPackets:int};LowerLimit\\(1050\\)=%{NUMBER:lowerThreshold:int};LimitRuleNum\\(1051\\)=%{NUMBER:ruleId:int};Event\\(1048\\)=%{DATA:eventMessage};'],
                             'log_explanation': '当连接数的并发数从达到上限恢复到下限时触发日志输出', 'log_recommended_action': '无'}]


    elif module == "DEV":

        if log_type_desc == "BOARD_INSERTED":
            pattern_logs = [
                {'patterns': ['Board was inserted on %{DATA:chassisNumberSlotNumberSlotNumber}, type is unknown.'],
                 'log_explanation': '有单板插入设备，但是单板类型未知',
                 'log_recommended_action': '单板插入设备后，需要一段时间才能完成启动，该段时间内，提示该日志，属于正常情况，无需处理'}]

        elif log_type_desc == "BOARD_REBOOT":
            pattern_logs = [{'patterns': ['Board is rebooting on %{DATA:chassisNumberSlotNumberSlotNumber}.'],
                             'log_explanation': '用户在重启指定slot，或者指定slot因为异常而重启',
                             'log_recommended_action': '1.      检查是否有用户在重启指定slot\n2.      如果没有用户重启，等待指定slot重新启动后，通过display version命令、对应指定slot信息中的Last reboot reason字段，查看重启原因\n3.      如果重启原因为异常重启，请联系技术支持'}]

        elif log_type_desc == "BOARD_REMOVED":
            pattern_logs = [{'patterns': [
                'Board was removed from %{DATA:chassisNumberSlotNumberSlotNumber}, type is %{DATA:cardType}.'],
                             'log_explanation': '一块LPU或者备用MPU被拔出。设备退出IRF',
                             'log_recommended_action': '1.      检查对应单板是否插紧\n2.      检查对应单板是否损坏\n3.      重新插入单板或更换单板\n4.      重新将设备加入IRF'}]

        elif log_type_desc == "BOARD_STATE_FAULT":
            pattern_logs = [{'patterns': [
                'Board state changed to Fault on %{DATA:chassisNumberSlotNumberSlotNumber}, type is %{DATA:cardType}.'],
                             'log_explanation': '单板在以下情况会处于Fault（故障）状态：\n·          单板处于启动阶段（正在初始化或者加载软件版本），单板不可用\n·          单板不能正常工作',
                             'log_recommended_action': '根据日志产生的情况，处理建议如下：\n·          对于第一种情况：单板型号不同，加载的软件版本不同，启动所需的时间不同。一般不超过10分钟，请以设备的实际情况为准\n·          对于第二种情况：请联系技术支持'}]

        elif log_type_desc == "BOARD_STATE_NORMAL":
            pattern_logs = [{'patterns': [
                'Board state changed to Normal on %{DATA:chassisNumberSlotNumberSlotNumber}, type is %{DATA:cardType}.'],
                             'log_explanation': '一块新插入的LPU或者备用MPU完成了初始化', 'log_recommended_action': '无'}]

        elif log_type_desc == "BOARD_STATE_STARTING":
            pattern_logs = [{'patterns': [
                'Board state changed to Starting on %{DATA:chassisNumberSlotNumberSlotNumber}, type is unknown.'],
                             'log_explanation': '单板处于启动阶段（正在初始化或者加载软件版本），不能正常工作',
                             'log_recommended_action': '1.      查看单板型号和设备型号是否适配\n2.      查看启动文件和设备软件版本以及硬件是否适配\n3.      请联系技术支持'}]

        elif log_type_desc == "CFCARD_INSERTED":
            pattern_logs = [{'patterns': [
                'CF card was inserted in %{DATA:chassisNumberSlotNumberSlotNumber} CF card slot %{NUMBER:cfCardSlotNumber:int}.'],
                             'log_explanation': '一块CF卡安装到了指定槽位', 'log_recommended_action': '无'}]

        elif log_type_desc == "CFCARD_REMOVED":
            pattern_logs = [{'patterns': [
                'CF card was removed from %{DATA:chassisNumberSlotNumberSlotNumber} CF card slot %{NUMBER:cfCardSlotNumber:int}.'],
                             'log_explanation': '一块CF卡被拔出',
                             'log_recommended_action': '1.      检查CF卡是否插紧\n2.      检查CF卡是否损坏\n3.      重新安装CF卡或更换CF卡'}]

        elif log_type_desc == "CHASSIS_REBOOT":
            pattern_logs = [{'patterns': ['Chassis %{NUMBER:chassisNumber:int} is rebooting now.'],
                             'log_explanation': '用户在重启成员设备，或者成员设备因为异常而重启',
                             'log_recommended_action': '1.      检查是否有用户在重启成员设备\n2.      如果没有用户重启，等待成员设备重新启动后，通过display version命令、对应成员设备单板信息中的Last reboot reason字段，查看重启原因\n3.      如果重启原因为异常重启，请联系技术支持'}]

        elif log_type_desc == "DEV_CLOCK_CHANGE":
            pattern_logs = [{'patterns': ['System clock changed from %{DATA:oldTime} to %{DATA:newTime}.'],
                             'log_explanation': '系统时间发生了变更', 'log_recommended_action': '无'}]

        elif log_type_desc == "DEV_FAULT_TOOLONG":
            pattern_logs = [{'patterns': [
                'Card in %{DATA:chassisNumberSlotNumberSlotNumber} is still in Fault state for %{NUMBER:timeDurationCardStayedFaultState:int} minutes.'],
                             'log_explanation': '单板长期处于Fault状态',
                             'log_recommended_action': '1.      重启单板尝试恢复\n2.      联系工程师分析解决'}]

        elif log_type_desc == "FAN_ABSENT":
            pattern_logs = [{'patterns': ['Fan %{NUMBER:fanTrayNumber:int} is absent.',
                                          'Chassis %{NUMBER:chassisNumber:int} fan %{NUMBER:fanTrayNumber:int} is absent.'],
                             'log_explanation': '指定位置没有风扇，或风扇被拔出',
                             'log_recommended_action': '1.      如果指定位置没有风扇，则可能因散热不好，引起设备温度升高，建议安装风扇\n2.      如果有风扇，检查风扇框是否插紧\n3.      检查风扇框是否损坏\n4.      重新安装风扇框或更换风扇框'}]

        elif log_type_desc == "FAN_DIRECTION_NOT_PREFERRED":
            pattern_logs = [{'patterns': [
                'Fan %{NUMBER:fanTrayNumber:int} airflow direction is not preferred on %{DATA:chassisNumberSlotNumberSlotNumber}, please check it.'],
                             'log_explanation': '风扇的风道方向不是用户期望的方向。风扇方向配置出错或者插错风扇',
                             'log_recommended_action': '1.      根据机房通风系统的风向，选择风向一致的型号的风扇\n2.      如果风扇风向和机房通风系统风向一致，请调整风扇风向的配置'}]

        elif log_type_desc == "FAN_FAILED":
            pattern_logs = [{'patterns': ['Fan %{NUMBER:fanTrayNumber:int} failed.',
                                          'Chassis %{NUMBER:chassisNumber:int} fan %{NUMBER:fanTrayNumber:int} failed.'],
                             'log_explanation': '风扇出现了故障，停止工作', 'log_recommended_action': '更换风扇'}]

        elif log_type_desc == "FAN_RECOVERED":
            pattern_logs = [{'patterns': ['Fan %{NUMBER:fanTrayNumber:int} recovered.',
                                          'Chassis %{NUMBER:chassisNumber:int} fan %{NUMBER:fanTrayNumber:int} recovered.'],
                             'log_explanation': '插入风扇，稍后，风扇转入正常工作状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAD_DETECT":
            pattern_logs = [{'patterns': ['Multi-active devices detected, please fix it.'],
                             'log_explanation': '当收到冲突消息的时候，检测到冲突，需要解决冲突问题',
                             'log_recommended_action': '1.      使用display irf查看当前IRF中有哪些成员设备，以便确定哪些成员设备分裂了\n2.      使用display irf link查看IRF链路信息，确认故障的IRF链路\n3.      手工修复状态为DOWN的IRF链路'}]

        elif log_type_desc == "MAD_PROC":
            pattern_logs = [{'patterns': [
                '%{DATA:protocolDetectedMadConflict} protocol detected MAD conflict: Local health value=%{NUMBER:currentHealthValueLocalIrf:int}, Peer health value=%{NUMBER:currentHealthValuePeerIrf:int}.'],
                             'log_explanation': '在IRF组网环境中，ARP、ND、LACP或BFD协议检测到MAD冲突。冲突发生时，记录本端IRF和对端IRF的健康值。取值为0时表示健康，取值越大越不健康',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POWER_ABSENT":
            pattern_logs = [{'patterns': ['Power %{NUMBER:powerSupplyNumber:int} is absent.',
                                          'Chassis %{NUMBER:chassisNumber:int} power %{NUMBER:powerSupplyNumber:int} is absent.'],
                             'log_explanation': '电源模块被拔出',
                             'log_recommended_action': '1.      检查电源是否插紧\n2.      检查电源是否损坏\n3.      重新安装电源或更换电源'}]

        elif log_type_desc == "POWER_FAILED":
            pattern_logs = [{'patterns': ['Power %{NUMBER:powerSupplyNumber:int} failed.',
                                          'Chassis %{NUMBER:chassisNumber:int} power %{NUMBER:powerSupplyNumber:int} failed.'],
                             'log_explanation': '电源模块出现故障', 'log_recommended_action': '更换电源'}]

        elif log_type_desc == "POWER_MONITOR_ABSENT":
            pattern_logs = [{'patterns': ['Power monitor unit %{NUMBER:powerMonitoringModuleNumber:int} is absent.',
                                          'Chassis %{NUMBER:chassisNumber:int} power monitor unit %{NUMBER:powerMonitoringModuleNumber:int} is absent.'],
                             'log_explanation': '电源监控模块被拔出',
                             'log_recommended_action': '1.      检查电源监控模块是否插紧\n2.      检查电源监控模块是否损坏\n3.      重新安装电源监控模块或更换电源监控模块'}]

        elif log_type_desc == "POWER_MONITOR_FAILED":
            pattern_logs = [{'patterns': ['Power monitor unit %{NUMBER:powerMonitoringModuleNumber:int} failed.',
                                          'Chassis %{NUMBER:chassisNumber:int} power monitor unit %{NUMBER:powerMonitoringModuleNumber:int} failed.'],
                             'log_explanation': '电源监控模块出现故障', 'log_recommended_action': '更换电源监控模块'}]

        elif log_type_desc == "POWER_MONITOR_RECOVERED":
            pattern_logs = [{'patterns': ['Power monitor unit %{NUMBER:powerMonitoringModuleNumber:int} recovered.',
                                          'Chassis %{NUMBER:chassisNumber:int} power monitor unit %{NUMBER:powerMonitoringModuleNumber:int} recovered.'],
                             'log_explanation': '电源监控模块插入后，状态从Failed或者Absent状态转换为Normal',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POWER_RECOVERED":
            pattern_logs = [{'patterns': ['Power %{NUMBER:powerSupplyNumber:int} recovered.',
                                          'Chassis %{NUMBER:chassisNumber:int} power %{NUMBER:powerSupplyNumber:int} recovered.'],
                             'log_explanation': '电源模块插入后，状态从Failed或者Absent状态转换为Normal', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPS_ABSENT":
            pattern_logs = [{'patterns': ['RPS %{NUMBER:rpsNumber:int} is absent.',
                                          'Chassis %{NUMBER:chassisNumber:int} RPS %{NUMBER:rpsNumber:int} is absent.'],
                             'log_explanation': '冗余电源模块被拔出',
                             'log_recommended_action': '1.      检查冗余电源模块是否插紧\n2.      检查冗余电源模块是否损坏\n3.      重新安装冗余电源模块或更换冗余电源模块'}]

        elif log_type_desc == "RPS_FAILED":
            pattern_logs = [{'patterns': ['RPS %{NUMBER:rpsNumber:int} failed.',
                                          'Chassis %{NUMBER:chassisNumber:int} RPS %{NUMBER:rpsNumber:int} failed.'],
                             'log_explanation': '冗余电源模块没供电或者故障',
                             'log_recommended_action': '1.      检查冗余电源线是否插紧\n2.      检查冗余电源模块是否故障\n3.      对于可插拔的冗余电源模块，请重新安装冗余电源模块或更换冗余电源模块'}]

        elif log_type_desc == "RPS_NORMAL":
            pattern_logs = [{'patterns': ['RPS %{NUMBER:rpsNumber:int} is normal.',
                                          'Chassis %{NUMBER:chassisNumber:int} RPS %{NUMBER:rpsNumber:int} is normal.'],
                             'log_explanation': '冗余电源模块插入后，状态正常', 'log_recommended_action': '无'}]

        elif log_type_desc == "SUBCARD_FAULT":
            pattern_logs = [{'patterns': [
                'Subcard state changed to Fault on %{DATA:chassisNumberSlotNumberSlotNumber} subslot %{NUMBER:subslotNumber:int}, type is %{DATA:subcardType}.'],
                             'log_explanation': '子卡重启，稍后，子卡状态转换为Fault，或者子卡故障',
                             'log_recommended_action': '1.      如果后续子卡状态可以变为Normal，则无需处理\n2.      如果子卡一直处于Falut状态，则子卡故障，更换子卡'}]

        elif log_type_desc == "SUBCARD_INSERTED":
            pattern_logs = [{'patterns': [
                'Subcard was inserted in %{DATA:chassisNumberSlotNumberSlotNumber} subslot %{NUMBER:subslotNumber:int}, type is %{DATA:subcardType}.'],
                             'log_explanation': '一块子卡安装到了指定槽位', 'log_recommended_action': '无'}]

        elif log_type_desc == "SUBCARD_REBOOT":
            pattern_logs = [{'patterns': [
                'Subcard is rebooting on %{DATA:chassisNumberSlotNumberSlotNumber} subslot %{NUMBER:subslotNumber:int}.'],
                             'log_explanation': '用户在重启子卡或者子卡因为运行异常自动重启',
                             'log_recommended_action': '如果子卡重启后能正常运行，则无需处理。如果您想进一步了解异常重启的原因或者子卡不断自动重启，请联系技术支持'}]

        elif log_type_desc == "SUBCARD_REMOVED":
            pattern_logs = [{'patterns': [
                'Subcard was removed from %{DATA:chassisNumberSlotNumberSlotNumber} subslot %{NUMBER:subslotNumber:int}, type is %{DATA:subcardType}.'],
                             'log_explanation': '一块子卡被拔出',
                             'log_recommended_action': '1.      检查子卡是否插紧\n2.      检查子卡是否损坏\n3.      重新安装子卡或更换子卡'}]

        elif log_type_desc == "SYSTEM_REBOOT":
            pattern_logs = [{'patterns': ['System is rebooting now.'], 'log_explanation': '用户在重启系统，或者系统因为异常而重启',
                             'log_recommended_action': '1.      检查是否有用户在重启系统\n2.      如果没有用户重启，等待系统重新启动后，通过display version命令显示信息中的Last reboot reason字段，查看重启原因\n3.      如果重启原因为异常重启，请联系技术支持'}]

        elif log_type_desc == "TEMPERATURE_ALARM":
            pattern_logs = [{'patterns': [
                'Temperature is greater than the high-temperature alarming threshold on sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature is greater than the high-temperature alarming threshold on %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature is greater than the high-temperature alarming threshold on %{DATA:chassisNumber} %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.'],
                             'log_explanation': '传感器温度超过了严重级（Alarm）高温告警门限。环境温度太高或者风扇异常',
                             'log_recommended_action': '1.      检查环境温度是否过高，保持设备环境正常通风\n2.      display fan命令检查风扇是否不在或故障，以及检查风扇实际是否运转。如果风扇不在位，安装风扇；如果风扇故障，更换风扇'}]

        elif log_type_desc == "TEMPERATURE_LOW":
            pattern_logs = [{'patterns': [
                'Temperature is less than the low-temperature threshold on sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature is less than the low-temperature threshold on %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature is less than the low-temperature threshold on %{DATA:chassisNumber} %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.'],
                             'log_explanation': '传感器温度低于低温告警门限', 'log_recommended_action': '环境温度过低，改善环境温度'}]

        elif log_type_desc == "TEMPERATURE_NORMAL":
            pattern_logs = [{'patterns': [
                'Temperature changed to normal on sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature changed to normal on %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature changed to normal on %{DATA:chassisNumber} %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.'],
                             'log_explanation': '传感器温度指示正常（大于低温告警门限，小于一般级高温告警门限）', 'log_recommended_action': '无'}]

        elif log_type_desc == "TEMPERATURE_SHUTDOWN":
            pattern_logs = [{'patterns': [
                'Temperature is greater than the high-temperature shutdown threshold on sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}. The slot will be powered off automatically.',
                'Temperature is greater than the high-temperature shutdown threshold on %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}. The slot will be powered off automatically.',
                'Temperature is greater than the high-temperature shutdown threshold on %{DATA:chassisNumber} %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}. The slot will be powered off automatically.'],
                             'log_explanation': '传感器温度高过了关断级高温告警门限，设备将自动关闭。环境温度太高或者风扇异常',
                             'log_recommended_action': '1.      检查环境温度是否过高，保持设备环境通风正常\n2.      display fan命令检查风扇是否不在或故障，以及检查风扇实际是否运转。如果风扇不在位，安装风扇；如果风扇故障，更换风扇'}]

        elif log_type_desc == "TEMPERATURE_WARNING":
            pattern_logs = [{'patterns': [
                'Temperature is greater than the high-temperature warning threshold on sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature is greater than the high-temperature warning threshold on %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.',
                'Temperature is greater than the high-temperature warning threshold on %{DATA:chassisNumber} %{DATA:slotNumber} sensor %{DATA:sensorType} %{NUMBER:sensorNumber:int}.'],
                             'log_explanation': '传感器温度高过了一般级高温告警门限。环境温度太高或者风扇异常',
                             'log_recommended_action': '1.      检查环境温度是否过高，保持设备环境通风正常\n2.      display fan命令检查风扇是否不在或故障，以及检查风扇实际是否运转。如果风扇不在位，安装风扇；如果风扇故障，更换风扇'}]

        elif log_type_desc == "TIMER_CREATE_FAILED_FIRST":
            pattern_logs = [{'patterns': [
                'The process with PID %{NUMBER:param0:int} failed to create a timer.Reason for the failure:%{DATA:param1}'],
                             'log_explanation': '进程第一次创建定时器失败以及失败的原因。为避免异常情况下，频繁打印该日志，系统对该日志采取抑制输出机制：\n·          进程第一次创建定时器失败时立即输出TIMER_CREATE_FAILED_FIRST日志\n·          超过15分钟后，如果该进程创建定时器再次失败，则输出日志TIMER_CREATE_FAILED_MORE，TIMER_CREATE_FAILED_MORE中会包含上次输出定时器创建失败日志的时间，以及上次输出定时器创建失败日志到本次输出定时器创建失败日志期间创建定时器失败的次数。15分钟内创建失败的日志会被抑制，不会输出',
                             'log_recommended_action': '如果进程对应的业务模块的功能受到影响，可重启设备尝试修复或者联系技术支持'}]

        elif log_type_desc == "TIMER_CREATE_FAILED_MORE":
            pattern_logs = [{'patterns': [
                'The process with PID %{NUMBER:param0:int} failed to create a timer:%{NUMBER:param1:int} consecutive failures since %{DATA:param2}.Reason for the failure:%{DATA:param3}'],
                             'log_explanation': '进程第一次创建定时器失败以及失败的原因。为避免异常情况下，频繁打印该日志，系统对该日志采取抑制输出机制：\n·          进程第一次创建定时器失败时立即输出TIMER_CREATE_FAILED_FIRST日志\n·          超过15分钟后，如果该进程创建定时器再次失败，则输出日志TIMER_CREATE_FAILED_MORE，TIMER_CREATE_FAILED_MORE中会包含上次输出定时器创建失败日志的时间，以及上次输出定时器创建失败日志到本次输出定时器创建失败日志期间创建定时器失败的次数。15分钟内创建失败的日志会被抑制，不会输出',
                             'log_recommended_action': '如果进程对应的业务模块的功能受到影响，可重启设备尝试修复或者联系技术支持'}]

        elif log_type_desc == " VCHK_VERSION_INCOMPATIBLE":
            pattern_logs = [{'patterns': [
                'Software version of %{DATA:chassisNumberSlotNumberSlotNumber} is incompatible with that of the MPU.'],
                             'log_explanation': 'PEX在启动过程中，检测到自己的启动软件包和父设备上运行的软件包版本不兼容，PEX会打印该信息并重启',
                             'log_recommended_action': '请设置与父设备当前版本兼容的软件包作为该PEX的下次启动软件包/加载软件包'}]


    elif module == "DHCP":

        if log_type_desc == "DHCP_NORESOURCES":
            pattern_logs = [{'patterns': [
                'Failed to apply filtering rules for DHCP packets because hardware resources are insufficient.'],
                             'log_explanation': '配置DHCP功能需要针对DHCP报文下发报文过滤规则。由于设备硬件资源不足，导致设置DHCP报文过滤规则失败',
                             'log_recommended_action': '如果设备业务占用硬件资源过多，可能会导致资源不足，需要释放一些资源，重新配置DHCP功能'}]

        elif log_type_desc == "DHCP_NOTSUPPORTED":
            pattern_logs = [
                {'patterns': ['Failed to apply filtering rules for DHCP packets because some rules are not supported.'],
                 'log_explanation': '配置DHCP功能需要针对DHCP报文下发DHCP报文过滤规则。由于设备不支持某些报文过滤规则，导致设置DHCP报文过滤规则失败',
                 'log_recommended_action': '无'}]


    elif module == "DHCPR":

        if log_type_desc == "DHCPR_SERVERCHANGE":
            pattern_logs = [{'patterns': [
                'Switched to the server at %{IP:ipAddressDhcpServer} \\(VPN name: %{DATA:vpnInformationDhcpServer}\\) because the current server did not respond.\nSwitched to the DHCP server at %{IP:ipAddressDhcpServerPublicNetwork} \\(Public network\\) because the current DHCP server did not respond.'],
                             'log_explanation': '因为DHCP中继无法从当前的DHCP服务器得到应答，所以DHCP中继切换到下一台指定VPN内或公网内的DHCP服务器申请IP地址',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "DHCPR_SWITCHMASTER":
            pattern_logs = [{'patterns': ['Switched to the master DHCP server at %{IP:ipAddressMasterDhcpServer}.'],
                             'log_explanation': 'DHCP中继可以配置延迟回切时间，如果当时生效的为备用服务器，在经过延迟时间，DHCP中继会切换到主用DHCP服务器来执行申请IP地址的操作',
                             'log_recommended_action': '无需处理'}]


    elif module == "DHCPS":

        if log_type_desc == "DHCPS_ALLOCATE_IP":
            pattern_logs = [{'patterns': [
                'DHCP server received a DHCP client’s request packet on interface %{DATA:nameInterfaceDhcpServerConfigured}, and allocated an IP address %{IP:ipv4AddressAssignedDhcpClient}\\(lease %{NUMBER:leaseDurationAssignedIpv4Address:int} seconds\\) for the DHCP client\\(MAC %{MAC:macAddressDhcpClient}\\) from %{DATA:nameAddressPoolAssignedIpv4AddressBelongs} pool.'],
                             'log_explanation': 'IPv4 DHCP服务器为IPv4 DHCP客户端分配一个ipv4地址租约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS_CONFLICT_IP":
            pattern_logs = [{'patterns': [
                'A conflict IP %{IP:ipv4AddressConflict} from %{DATA:nameAddressPoolConflictingIpv4AddressBelongs} pool was detected by DHCP server on interface %{DATA:nameInterfaceDhcpServerConfigured}.'],
                             'log_explanation': 'IPv4 DHCP服务器从地址池中删除一个冲突地址', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS_EXTEND_IP":
            pattern_logs = [{'patterns': [
                "DHCP server received a DHCP client’s request packet on interface %{DATA:nameInterfaceDhcpServerConfigured}, and extended lease from %{DATA:nameAddressPoolClient'sIpv4AddressBelongs} pool for the DHCP client \\(IP %{IP:ipv4AddressDhcpClient}, MAC %{MAC:macAddressDhcpClient}\\)."],
                             'log_explanation': 'IPv4 DHCP服务器为IPv4 DHCP客户端续约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS_RECLAIM_IP":
            pattern_logs = [{'patterns': [
                'DHCP server reclaimed a %{DATA:nameAddressPoolAssignedIpv4AddressBelongs} pool’s lease\\(IP %{IP:ipv4AddressAssignedDhcpClient}, lease %{NUMBER:leaseDurationAssignedIpv4Address:int} seconds\\), which is allocated for the DHCP client \\(MAC %{MAC:macAddressDhcpClient}\\).'],
                             'log_explanation': 'IPv4 DHCP服务器回收一个分配给IPv4 DHCP客户端的地址租约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS_VERIFY_CLASS":
            pattern_logs = [{'patterns': [
                'Illegal DHCP client-PacketType=%{DATA:typePacket}-ClientAddress=%{MAC:hardwareAddressDhcpClient};'],
                             'log_explanation': 'IPv4 DHCP服务器对客户端报文白名单验证不通过',
                             'log_recommended_action': '确认该DHCP客户端是否合法'}]


    elif module == "DHCPSP6":

        if log_type_desc == "DHCPSP6_FILE":
            pattern_logs = [{'patterns': ['Failed to save DHCP client information due to lack of storage resources.'],
                             'log_explanation': '因为磁盘空间不足导致DHCPv6 snooping保存客户端信息到文件失败',
                             'log_recommended_action': '删除其他文件，使有空间保存此文件'}]


    elif module == "DHCPS6":

        if log_type_desc == "DHCPS6_ALLOCATE_ADDRESS":
            pattern_logs = [{'patterns': [
                'DHCPv6 server received a DHCPv6 client’s request packet on interface %{DATA:nameInterfaceDhcpv6ServerConfigured}, and allocated an IPv6 address %{IP:ipv6AddressAssignedDhcpv6Client} \\(lease %{NUMBER:leaseDurationAssignedIpv6Address:int} seconds\\) for the DHCP client\\(DUID %{DATA:duidDhcpv6Client}, IAID %{DATA:iaidDhcpv6Client}\\) from %{DATA:nameAddressPoolAssignedIpv6AddressBelongs} pool.'],
                             'log_explanation': 'IPv6 DHCP服务器为IPv6 DHCP客户端分配一个IPv6地址租约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS6_ALLOCATE_PREFIX":
            pattern_logs = [{'patterns': [
                'DHCPv6 server received a DHCPv6 client’s request packet on interface %{DATA:nameInterfaceDhcpv6ServerConfigured}, and allocated an IPv6 prefix %{IP:ipv6PrefixAssignedDhcpv6Client} \\(lease %{NUMBER:leaseDurationAssignedIpv6Prefix:int} seconds\\) for the DHCP client\\(DUID %{DATA:duidDhcpv6Client}, IAID %{DATA:iaidDhcpv6Client}\\) from %{DATA:nameAddressPoolAssignedIpv6PrefixBelongs} pool.'],
                             'log_explanation': 'IPv6 DHCP服务器为IPv6 DHCP客户端分配一个IPv6前缀地址租约',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS6_CONFLICT_ADDRESS":
            pattern_logs = [{'patterns': [
                'A conflict IPv6 address %{IP:param0} from %{DATA:param1} pool was detected by DHCPv6 server on interface %{DATA:param2}.'],
                             'log_explanation': 'IPv6 DHCP服务器从地址池删除一个冲突地址', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS6_EXTEND_ADDRESS":
            pattern_logs = [{'patterns': [
                "DHCPv6 server received a DHCP client’s request packet on interface %{DATA:nameInterfaceDhcpv6ServerConfigured}, and extended lease from %{DATA:nameAddressPoolClient'sIpv6AddressBelongs} pool for the DHCP client \\(IPv6 address %{IP:ipv6AddressDhcpv6Client}, DUID %{DATA:duidDhcpv6Client}, IAID %{DATA:iaidDhcpv6Client}\\)."],
                             'log_explanation': 'IPv6 DHCP服务器为IPv6 DHCP客户端地址续约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS6_EXTEND_PREFIX":
            pattern_logs = [{'patterns': [
                "DHCPv6 server received a DHCP client’s request packet on interface %{DATA:nameInterfaceDhcpv6ServerConfigured}, and extended lease from %{DATA:nameAddressPoolClient'sIpv6PrefixBelongs} pool for the DHCP client \\(IPv6 prefix %{IP:ipv6PrefixDhcpv6Client}, DUID %{DATA:duidDhcpv6Client}, IAID %{DATA:iaidDhcpv6Client}\\)."],
                             'log_explanation': 'IPv6 DHCP服务器为IPv6 DHCP客户端前缀地址续约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS6_RECLAIM_ADDRESS":
            pattern_logs = [{'patterns': [
                'DHCPv6 server reclaimed a %{DATA:nameAddressPoolAssignedIpv6AddressBelongs} pool’s lease\\(IPv6 address %{IP:ipv6AddressAssignedDhcpv6Client}, lease %{NUMBER:leaseDurationAssignedIpv6Address:int} seconds\\), which is allocated for the DHCPv6 client \\(DUID %{DATA:duidDhcpv6Client}, IAID %{DATA:iaidDhcpv6Client}\\).'],
                             'log_explanation': 'IPv6 DHCP服务器回收一个分配给IPv6客户端的地址租约', 'log_recommended_action': '无'}]

        elif log_type_desc == "DHCPS6_RECLAIM_PREFIX":
            pattern_logs = [{'patterns': [
                'DHCPv6 server reclaimed a %{DATA:nameAddressPoolAssignedIpv6PrefixBelongs} pool’s lease\\(IPv6 prefix %{IP:ipv6PrefixAssignedDhcpv6Client}, lease %{NUMBER:leaseDurationAssignedIpv6Prefix:int} seconds\\), which is allocated for the DHCPv6 client \\(DUID %{DATA:duidDhcpv6Client}, IAID %{DATA:iaidDhcpv6Client}\\).'],
                             'log_explanation': 'IPv6 DHCP服务器回收一个分配给IPv6客户端的前缀地址租约', 'log_recommended_action': '无'}]


    elif module == "DIAG":

        if log_type_desc == "CPU_MINOR_THRESHOLD":
            pattern_logs = [{'patterns': ['CPU usage recovered to normal state.'],
                             'log_explanation': '当设备处于CPU低级别告警状态，并且采样值小于或等于恢复门限时，解除CPU低级别告警状态，CPU使用率恢复到正常',
                             'log_recommended_action': '根据提示信息操作设备，合理使用CPU资源'}, {'patterns': [
                'CPU usage is in minor alarm state.\nCPU usage: %{NUMBER:cpuUsageLastMinute:int}% in last 1 minute.\nCPU usage thresholds:\nMinor: %{NUMBER:minorCpuUsageAlarmThreshold:int}%\nSevere: %{NUMBER:severeCpuUsageAlarmThreshold:int}%\nRecovery: %{NUMBER:cpuUsageRecoveryThreshold:int}%\nProcess info:\nJID      PID     PRI      State     FDs     HH:MM:SS   CPU       Name\n%{NUMBER:jobIdProcess:int} %{NUMBER:pidProcess:int} %{NUMBER:priorityProcess:int} %{DATA:statusProcess} %{NUMBER:numberFileHandles:int} %{DATA:runningTimeProcess}          %{DATA:cpuUsageProcess}  %{DATA:nameProcess}\nCore states:\nID                 Idle          User       Kernel     Interrupt  Busy\nCPU%{NUMBER:coreId:int}   %{DATA:idleTime}   %{DATA:timeUsedProcessesUserSpace}   %{DATA:timeUsedKernelThreads}   %{DATA:timeUsedInterrupts}   %{DATA:totalTimeUsed}'],
                                                                                 'log_explanation': '当CPU使用率的采样值从小于/等于变成大于低级别告警门限时，设备进入CPU低级别告警状态，并定期输出该日志，直到CPU低级别告警状态解除',
                                                                                 'log_recommended_action': '根据提示信息操作设备，合理使用CPU资源'}]

        elif log_type_desc == "CPU_RECOVERY":
            pattern_logs = [{'patterns': ['CPU usage severe alarm removed.'],
                             'log_explanation': '当设备处于CPU高级别告警状态，并且采样值小于或等于低级别告警门限时，解除CPU高级别告警状态，输出该日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "CPU_THRESHOLD":
            pattern_logs = [{'patterns': [
                'CPU usage is in severe alarm state.\nCPU usage: %{NUMBER:cpuUsageLastMinute:int}% in last 1 minute.\nCPU usage thresholds:\nMinor: %{NUMBER:minorCpuUsageAlarmThreshold:int}%\nSevere: %{NUMBER:severeCpuUsageAlarmThreshold:int}%\nRecovery: %{NUMBER:cpuUsageRecoveryThreshold:int}%\nProcess info:\nJID      PID     PRI      State     FDs     HH:MM:SS   CPU       Name\n%{NUMBER:jobIdProcess:int} %{NUMBER:pidProcess:int} %{NUMBER:priorityProcess:int} %{DATA:statusProcess} %{NUMBER:numberFileHandles:int} %{DATA:runningTimeProcess}         %{DATA:cpuUsageProcess}   %{DATA:nameProcess}\nCore states:\nID                 Idle          User       Kernel     Interrupt  Busy\nCPU%{NUMBER:coreId:int}   %{DATA:idleTime}   %{DATA:timeUsedProcessesUserSpace}   %{DATA:timeUsedKernelThreads}   %{DATA:timeUsedInterrupts}   %{DATA:totalTimeUsed}'],
                             'log_explanation': '当CPU使用率的采样值从小于/等于变成大于高级别告警门限时，设备进入CPU高级别告警状态，并定期输出该日志，直到CPU高级别告警状态解除',
                             'log_recommended_action': '请使用display current-configuration | include \\"monitor cpu-usage\\"命令查看CPU的告警门限，如果门限设置不合适，请使用monitor cpu-usage命令修改'}]

        elif log_type_desc == "CPU_USAGE_LASTMINUTE":
            pattern_logs = [{'patterns': ['CPU usage was %{DATA:cpuUsagePercentage} in last minute.'],
                             'log_explanation': 'CPU最近1分钟的平均利用率', 'log_recommended_action': '无'}]

        elif log_type_desc == "MEM_ALERT":
            pattern_logs = [{'patterns': [
                'system memory info:\ntotal           used             free        shared       buffers       cached\nMem:    %{NUMBER:totalSizeAllocatablePhysicalMemory:int}    %{NUMBER:sizePhysicalMemoryUsedSystem:int}    %{NUMBER:sizeFreePhysicalMemorySystem:int}    %{NUMBER:totalSizePhysicalMemorySharedProcesses:int}    %{NUMBER:sizePhysicalMemoryUsedBuffers:int}    %{NUMBER:sizePhysicalMemoryUsedCaches:int}\n-/+ buffers/cache:    %{NUMBER:-/+Buffers/cache:int}    %{NUMBER:-/+Buffers/cache:int}\nSwap:    %{NUMBER:totalSizeSwapMemory:int}    %{NUMBER:sizeUsedSwapMemory:int}    %{NUMBER:sizeFreeSwapMemory:int}\nLowmem: %{NUMBER:totalSizeLowMemory:int}  %{NUMBER:sizeUsedLowMemory:int}    %{NUMBER:sizeFreeLowMemory:int}'],
                             'log_explanation': '内存告警。当已使用的内存大于或等于一级、二级或三级内存告警门限时，系统会输出该信息，告知用户内存的具体使用情况',
                             'log_recommended_action': '1.      请使用display memory-threshold命令查看内存的一级、二级、三级告警门限。如果门限设置不合适，请使用memory-threshold命令修改\n2.      检查ARP、路由表信息，排除设备受到非法攻击可能\n3.      检查和优化组网，减少路由条目或者更换更高规格的设备'}]

        elif log_type_desc == "MEM_BELOW_THRESHOLD":
            pattern_logs = [{'patterns': ['Memory usage has dropped below %{DATA:memoryUsageThresholdName} threshold.'],
                             'log_explanation': '内存告警解除。当系统剩余空闲内存大于内存恢复门限时，系统会输出该信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "MEM_EXCEED_THRESHOLD":
            pattern_logs = [{'patterns': ['Memory %{DATA:memoryUsageThresholdName} threshold has been exceeded.'],
                             'log_explanation': '内存告警。当已使用的内存大于或等于一级、二级或三级内存告警门限时，系统会输出该信息，并通知各业务模块进行自动修复：比如，不再申请新的内存或者释放部分内存',
                             'log_recommended_action': '1.      请使用display memory-threshold命令查看内存的一级、二级、三级告警门限。如果门限设置不合适，请使用memory-threshold命令修改\n2.      检查ARP、路由表信息，排除设备受到非法攻击可能\n3.      检查和优化组网，减少路由条目或者更换更高规格的设备'}]

        elif log_type_desc == "MEM_USAGE":
            pattern_logs = [{'patterns': ['Current memory usage is %{DATA:memoryUsagePercentage}.'],
                             'log_explanation': '设备当前的内存利用率', 'log_recommended_action': '无'}]


    elif module == "DLDP":

        if log_type_desc == "DLDP_AUTHENTICATION_FAILED":
            pattern_logs = [{'patterns': [
                'The DLDP packet failed the authentication because of unmatched %{DATA:authenticationField} field.'],
                             'log_explanation': '报文验证失败。可能的原因包括：验证类型不匹配、验证字不匹配、通告间隔不匹配',
                             'log_recommended_action': '检查DLDP验证类型、验证字和通告间隔是否与对端一致'}]

        elif log_type_desc == "DLDP_LINK_BIDIRECTIONAL":
            pattern_logs = [{'patterns': ['DLDP detected a bidirectional link on interface %{DATA:interfaceName}.'],
                             'log_explanation': 'DLDP在接口上检测到双向链路', 'log_recommended_action': '无'}]

        elif log_type_desc == "DLDP_LINK_SHUTMODECHG":
            pattern_logs = [{'patterns': [
                'DLDP automatically %{DATA:actionAccordingPortShutdownMode} interface %{DATA:interfaceName} because the port shutdown mode was changed %{DATA:shutdownModeChange}.'],
                             'log_explanation': '因为DLDP单通关闭模式发生变化，端口被关闭或打开', 'log_recommended_action': '无'}]

        elif log_type_desc == "DLDP_LINK_UNIDIRECTIONAL":
            pattern_logs = [{'patterns': [
                'DLDP detected a unidirectional link on interface %{DATA:interfaceName}. %{DATA:actionAccordingPortShutdownMode}.'],
                             'log_explanation': 'DLDP在接口上检测到单向链路', 'log_recommended_action': '检查线缆是否错接、脱落或者出现其他故障'}]

        elif log_type_desc == "DLDP_NEIGHBOR_AGED":
            pattern_logs = [{'patterns': [
                "A neighbor on interface %{DATA:interfaceName} was deleted because the neighbor was aged. The neighbor's system MAC is %{MAC:macAddress}, and the port index is %{NUMBER:portIndex:int}."],
                             'log_explanation': '接口删除了一个已老化的邻居', 'log_recommended_action': '无'}]

        elif log_type_desc == "DLDP_NEIGHBOR_CONFIRMED":
            pattern_logs = [{'patterns': [
                "A neighbor was confirmed on interface %{DATA:interfaceName}. The neighbor's system MAC is %{MAC:macAddress}, and the port index is %{NUMBER:portIndex:int}."],
                             'log_explanation': '接口检测到一个处于确定状态的邻居', 'log_recommended_action': '无'}]

        elif log_type_desc == "DLDP_NEIGHBOR_DELETED":
            pattern_logs = [{'patterns': [
                "A neighbor on interface %{DATA:interfaceName} was deleted because a %{DATA:packetType} packet arrived. The neighbor's system MAC is %{MAC:macAddress}, and the port index is %{NUMBER:portIndex:int}."],
                             'log_explanation': '由于收到了Disable报文或LinkDown报文，因此接口删除一个处于确定状态的邻居',
                             'log_recommended_action': '无'}]


    elif module == "DOT1X":

        if log_type_desc == "DOT1X_CONFIG_NOTSUPPORT":
            pattern_logs = [{'patterns': ['802.1X is not supported on interface %{DATA:interfaceTypeNumber}.'],
                             'log_explanation': '接口不支持802.1X特性', 'log_recommended_action': '无'}]

        elif log_type_desc == "DOT1X_LOGIN_FAILURE":
            pattern_logs = [{'patterns': ['User failed 802.1X authentication. Reason: %{DATA:failureCause}.'],
                             'log_explanation': '用户802.1X认证失败', 'log_recommended_action': '查看失败原因并修改相关配置'}]

        elif log_type_desc == "DOT1X_LOGIN_SUCC":
            pattern_logs = [
                {'patterns': ['User passed 802.1X authentication and came online.'], 'log_explanation': '802.1X用户认证成功',
                 'log_recommended_action': '无'},
                {'patterns': ['The user that failed 802.1X authentication passed open authentication and came online.'],
                 'log_explanation': '802.1X认证失败但通过开放认证模式认证成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "DOT1X_LOGOFF":
            pattern_logs = [{'patterns': ['802.1X user was logged off.'], 'log_explanation': '802.1X用户正常下线',
                             'log_recommended_action': '无'},
                            {'patterns': ['802.1X open user was logged off.'], 'log_explanation': '802.1X open用户正常下线',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "DOT1X_LOGOFF_ABNORMAL":
            pattern_logs = [{'patterns': ['802.1X user was logged off abnormally.'], 'log_explanation': '802.1X用户异常下线',
                             'log_recommended_action': '查看异常下线原因或进行后续操作'},
                            {'patterns': ['802.1X open user was logged off abnormally.'],
                             'log_explanation': '802.1X open用户异常下线', 'log_recommended_action': '查看异常下线原因或进行后续操作'}]

        elif log_type_desc == "DOT1X_MACBINDING_EXIST":
            pattern_logs = [
                {'patterns': ['MAC address was already bound to interface %{DATA:typeNumberInterfaceMacAddressBound}.'],
                 'log_explanation': '用户MAC地址已绑定在其它端口，用户无法上线', 'log_recommended_action': '在其它端口取消MAC地址绑定'}]

        elif log_type_desc == "DOT1X_NOTENOUGH_EADFREEIP_RES":
            pattern_logs = [{'patterns': [
                'Failed to assign a rule for free IP %{IP:freeIp} on interface %{DATA:interfaceTypeNumber} due to lack of ACL resources.'],
                             'log_explanation': '当在接口上使能802.1X特性时，由于ACL资源不足，设备在接口上下发free IP失败',
                             'log_recommended_action': '暂不使能802.1X，之后尝试重新使能802.1X'}]

        elif log_type_desc == "DOT1X_NOTENOUGH_EADFREEMSEG_RES":
            pattern_logs = [{'patterns': [
                'Failed to assign a rule for free microsegment %{NUMBER:param0:int} on interface %{DATA:param1} due to lack of ACL resources.'],
                             'log_explanation': '当在接口上使能802.1X特性时，由于ACL资源不足，设备在接口上下发免认证微分段失败',
                             'log_recommended_action': '暂不使能802.1X，之后尝试重新使能802.1X'}]

        elif log_type_desc == "DOT1X_NOTENOUGH_EADFREERULE_RES":
            pattern_logs = [{'patterns': [
                'Failed to assign a rule for permitting DHCP and DNS packets on interface %{DATA:interfaceTypeNumber} due to lack of ACL resources.'],
                             'log_explanation': '当在接口上使能802.1X特性时，由于ACL资源不足，设备不能下发允许该接口上DHCP协议和DNS协议报文通过的规则',
                             'log_recommended_action': '暂不使能802.1X，之后尝试重新使能802.1X'}]

        elif log_type_desc == "DOT1X_NOTENOUGH_EADMACREDIR_RES":
            pattern_logs = [{'patterns': [
                'Failed to assign a rule for redirecting HTTP packets with source MAC address %{MAC:sourceMacAddressHttpPackets} on interface %{DATA:interfaceTypeNumber}.'],
                             'log_explanation': '当在接口上使能802.1X特性时，由于ACL资源不足，设备不能重定向在指定接口上收到的源MAC地址为特定地址的HTTP报文',
                             'log_recommended_action': '暂不使能802.1X，之后尝试重新使能802.1X'}]

        elif log_type_desc == "DOT1X_NOTENOUGH_EADPORTREDIR_RES":
            pattern_logs = [{'patterns': [
                'Failed to assign a rule for redirecting HTTP packets on interface %{DATA:interfaceTypeNumber} due to lack of ACL resources.'],
                             'log_explanation': '当在接口上使能802.1X特性时，由于ACL资源不足，设备不能指定规则允许该接口重定向HTTP报文',
                             'log_recommended_action': '暂不使能802.1X，之后尝试重新使能802.1X'}]

        elif log_type_desc == "DOT1X_NOTENOUGH_ENABLEDOT1X_RES":
            pattern_logs = [{'patterns': [
                'Failed to enable 802.1X on interface %{DATA:interfaceTypeNumber} due to lack of ACL resources.'],
                             'log_explanation': '因为ACL资源不足，不能配置接口的802.1X特性',
                             'log_recommended_action': '暂不使能802.1X，之后尝试重新使能802.1X'}]

        elif log_type_desc == "DOT1X_PEXAGG_NOMEMBER_RES":
            pattern_logs = [{'patterns': [
                'Failed to enable 802.1X on interface %{DATA:interfaceTypeNumber} because the Layer 2 extended-link aggregate interface does not have member ports.'],
                             'log_explanation': '因为PEX二层聚合口不存在成员口，不能配置接口的802.1X特性',
                             'log_recommended_action': '暂不使能802.1X，PEX二层聚合口添加成员口后重新使能802.1X'}]

        elif log_type_desc == "DOT1X_SMARTON_FAILURE":
            pattern_logs = [{'patterns': ['User failed SmartOn authentication because %{DATA:param2}.'],
                             'log_explanation': 'SmartOn认证失败，及其原因', 'log_recommended_action': '根据失败原因修改相关配置'}]

        elif log_type_desc == "DOT1X_UNICAST_NOT_EFFECTIVE":
            pattern_logs = [{'patterns': [
                'The unicast trigger feature is enabled but is not effective on interface %{DATA:interfaceTypeNumber}.'],
                             'log_explanation': '单播触发特性在接口上不生效，因为该接口不支持单播触发特性',
                             'log_recommended_action': '更换到支持单播触发功能的接口上对用户进行802.1X认证'}]


    elif module == "DRNI":

        if log_type_desc == "DRNI_AUTORECOVERY_TIMEOUT":
            pattern_logs = [
                {'patterns': ['The reload delay timer timed out. Please check configuration of the DR system.'],
                 'log_explanation': 'DR系统自动恢复定时器超时，DR系统仅一台设备启动或DR系统出现双主情况',
                 'log_recommended_action': '·          检查对端DR设备是否正常启动\n·          检查IPL和Keepalive链路是否正常\n·          检查自动恢复定时器配置值是否过小'}]

        elif log_type_desc == "DRNI_GLBCHECK_CONSISTENCY":
            pattern_logs = [{'patterns': [
                'Finished global type %{NUMBER:configurationConsistencyCheckType:int} configuration consistency check. No inconsistency exists.'],
                             'log_explanation': '分布式聚合全局配置一致性检查结果一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_GLBCHECK_INCONSISTENCY":
            pattern_logs = [{'patterns': [
                'Detected global type %{NUMBER:configurationConsistencyCheckType:int} configuration inconsistency.'],
                             'log_explanation': '分布式聚合全局配置一致性检查结果不一致',
                             'log_recommended_action': '·          Type 1类型的全局配置不一致，通过display drni consistency命令查看两端设备配置信息，修改配置为一致\n·          Type 2类型的全局配置不一致，建议两端设备配置为一致'}]

        elif log_type_desc == "DRNI_IFCHECK_CONSISTENCY":
            pattern_logs = [{'patterns': [
                'Finished DR interface %{DATA:layer2AggregateInterfaceName} type %{NUMBER:configurationConsistencyCheckType:int} configuration consistency check. No inconsistency exists.'],
                             'log_explanation': '分布式聚合接口配置一致性接口检查结果一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFCHECK_INCONSISTENCY":
            pattern_logs = [{'patterns': [
                'Detected type %{NUMBER:layer2AggregateInterfaceName:int} configuration inconsistency on interface %{DATA:configurationConsistencyCheckType}.'],
                             'log_explanation': '分布式聚合接口配置一致性检查不一致',
                             'log_recommended_action': '·          Type 1类型的接口配置不一致，通过display drni consistency命令查看两端设备配置信息，修改配置为一致\n·          Type 2类型的接口配置不一致，建议两端设备配置为一致'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_BIND":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:layer2AggregateInterfaceName} was assigned to DR group %{NUMBER:drGroupNumber:int}.'],
                             'log_explanation': '聚合接口加入分布式聚合组，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_GLOBALDOWN":
            pattern_logs = [{'patterns': ['The state of DR group %{NUMBER:drGroupNumber:int} changed to down.'],
                             'log_explanation': 'DR组状态变为DOWN，触发该日志的原因为两台DR设备上同一DR组的DR接口的成员端口都变为未选中状态',
                             'log_recommended_action': '检查DR设备的系统配置，系统优先级、系统MAC地址、系统编号是否已配置且一致'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_GLOBALUP":
            pattern_logs = [{'patterns': ['The state of DR group %{NUMBER:drGroupNumber:int} changed to up.'],
                             'log_explanation': 'DR组状态变为UP，触发该日志的原因为两台DR设备上同一DR组的DR接口中第一次有成员端口变为被选中状态',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_MAC_CHANGE":
            pattern_logs = [{'patterns': [
                "Local DR interface %{DATA:layer2AggregateInterfaceName}'s system MAC address changed to %{DATA:systemMacAddress}. Please ensure that the configuration is consistent with that of the peer DR interface."],
                             'log_explanation': '用户修改DR接口系统MAC地址', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_NOSELECTED":
            pattern_logs = [{'patterns': [
                'Local DR interface %{DATA:layer2AggregateInterfaceName} in DR group %{NUMBER:drGroupNumber:int} does not have Selected member ports because %{DATA:causeStateDrInterface}.'],
                             'log_explanation': '本端DR接口对应的聚合组内无选中端口', 'log_recommended_action': '检查聚合组成员端口配置或者线缆连接情况'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_PEER_NOSELECTED":
            pattern_logs = [{'patterns': [
                'Peer DR interface in DR group %{NUMBER:drGroupNumber:int} does not have Selected member ports.'],
                             'log_explanation': '对端DR接口对应的聚合组内无选中端口',
                             'log_recommended_action': '检查对端聚合组成员端口配置或者线缆连接情况'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_PEER_SELECTED":
            pattern_logs = [
                {'patterns': ['Peer DR interface in DR group %{NUMBER:drGroupNumber:int} has Selected member ports.'],
                 'log_explanation': '对端DR接口对应的聚合组内存在选中端口', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_PRIORITY_CHANGE":
            pattern_logs = [{'patterns': [
                "DR interface %{DATA:layer2AggregateInterfaceName}'s system priority changed to %{NUMBER:newSystemPriority:int}. Please ensure that the configuration is consistent with that of the peer DR interface."],
                             'log_explanation': '用户修改DR接口的系统优先级', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_SELECTED":
            pattern_logs = [{'patterns': [
                'Local DR interface %{DATA:layer2AggregateInterfaceName} in DR group %{NUMBER:drGroupNumber:int} has Selected member ports.'],
                             'log_explanation': 'DR接口对应的聚合组内存在选中端口', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_DR_UNBIND":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:layer2AggregateInterfaceName} was removed from DR group %{NUMBER:drGroupNumber:int}.'],
                             'log_explanation': '聚合接口退出DR组，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_IPP_BIND":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:layer2AggregateInterfaceName} was configured as IPP %{NUMBER:ippNumber:int}.'],
                             'log_explanation': '聚合接口配置为IPP口，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_IPP_DOWN":
            pattern_logs = [
                {'patterns': ['IPP %{DATA:layer2AggregateInterfaceName} went down because %{DATA:causeStateIpp}.'],
                 'log_explanation': 'IPP口变为DOWN',
                 'log_recommended_action': '·          检查DR设备的系统配置，系统优先级、系统MAC地址、系统编号、认证密码、序列号校验功能状态，是否已配置且一致\n·          检查配置为IPP口的二层聚合接口状态'}]

        elif log_type_desc == "DRNI_IFEVENT_IPP_UNBIND":
            pattern_logs = [{'patterns': [
                'Configuration for IPP %{NUMBER:ippNumber:int} was removed from interface %{DATA:layer2AggregateInterfaceName}.'],
                             'log_explanation': '删除IPP口，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IFEVENT_IPP_UP":
            pattern_logs = [{'patterns': ['IPP %{DATA:layer2AggregateInterfaceName} came up.'],
                             'log_explanation': 'IPP口变为UP状态，触发该日志的原因为DR系统两端能正常收发DRCP协议报文',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_IPP_BLOCK":
            pattern_logs = [{'patterns': ['The status of IPP %{DATA:layer2AggregateInterfaceName} changed to blocked.'],
                             'log_explanation': 'IPP口变为阻塞状态，该状态下IPP口仅能收发协议报文，不能收发数据报文。触发该日志的原因为当设备有角色且IPP口down时，IPP口变为阻塞状态',
                             'log_recommended_action': '·          检查IPL连接线缆是否正常\n·          检查IPL两端配置是否一致'}]

        elif log_type_desc == "DRNI_IPP_UNBLOCK":
            pattern_logs = [
                {'patterns': ['The status of IPP %{DATA:layer2AggregateInterfaceName} changed to unblocked.'],
                 'log_explanation': 'IPP口变为非阻塞状态，该状态下IPP口可以正常收发协议报文和数据报文。触发该日志的原因为当设备有角色且IPP口up时，IPP口变为非阻塞状态',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_KEEPALIVEINTERVAL_MISMATCH":
            pattern_logs = [
                {'patterns': ['Keepalive interval on the local DR device is different from that on the neighbor.'],
                 'log_explanation': 'DR系统两端的Keepalive报文发包间隔配置的不一致，会导致一端快速超时，出现误检测，触发该日志的原因为DR系统两端配置的Keepalive报文发包间隔不一致',
                 'log_recommended_action': '将DR系统两端的Keepalive报文发包间隔配置一致'}]

        elif log_type_desc == "DRNI_KEEPALIVELINK_DOWN":
            pattern_logs = [
                {'patterns': ['Keepalive link went down because %{DATA:causeStateKeepaliveLinkRecommendedRemedy}.'],
                 'log_explanation': 'Keepalive链路变为DOWN状态',
                 'log_recommended_action': '·          检查设备角色\n·          检查DR设备的Keepalive配置，两端源IP、目的IP是否匹配\n·          检查所选取的三层链路状态'}]

        elif log_type_desc == "DRNI_KEEPALIVELINK_UP":
            pattern_logs = [{'patterns': ['Keepalive link came up.'],
                             'log_explanation': 'KEEPALIVE链路变为UP状态，触发该日志的原因为DR系统两端能正常收发Keepalive协议报文',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_DEVICE_MADDOWN":
            pattern_logs = [
                {'patterns': ['%{DATA:param0} will change to the DRNI MAD DOWN state because %{DATA:param1}.'],
                 'log_explanation': '不同原因触发设备进行DRNI MAD检测时，设备会根据触发原因和当前配置关闭相应业务接口',
                 'log_recommended_action': '检查IPL两端配置'}]

        elif log_type_desc == "DRNI_DEVICE_MADRECOVERY":
            pattern_logs = [
                {'patterns': ['All service interfaces on the device will be recovered from the DRNI MAD DOWN state.'],
                 'log_explanation': '设备将会开启所有处于DRNI MAD DOWN状态的业务接口', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_SYSEVENT_DEVICEROLE_CHANGE":
            pattern_logs = [{'patterns': [
                'Device role changed from %{DATA:oldDeviceRole} to %{DATA:newDeviceRole} for %{DATA:reasonRoleChange}.'],
                             'log_explanation': 'DR设备角色变化及触发原因', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_SYSEVENT_MAC_CHANGE":
            pattern_logs = [{'patterns': [
                'System MAC address changed from %{DATA:oldSystemMacAddress} to %{DATA:newSystemMacAddress}.'],
                             'log_explanation': '分布式聚合系统MAC变化，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_SYSEVENT_MODE_CHANGE":
            pattern_logs = [{'patterns': ["The device's working mode changed to %{DATA:workingModeDevice}."],
                             'log_explanation': 'DR设备工作模式变化，触发原因为DR系统分裂或者合并', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_SYSEVENT_NUMBER_CHANGE":
            pattern_logs = [
                {'patterns': ['System number changed from %{DATA:oldSystemNumber} to %{DATA:newSystemNumber}.'],
                 'log_explanation': '分布式聚合系统编号变化，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]

        elif log_type_desc == "DRNI_SYSEVENT_PRIORITY_CHANGE":
            pattern_logs = [{'patterns': [
                'System priority changed from %{NUMBER:oldSystemPriority:int} to %{NUMBER:newSystemPriority:int}.'],
                             'log_explanation': '分布式聚合系统优先级改变，触发该日志的原因为用户设置', 'log_recommended_action': '无'}]


    elif module == "EDEV":

        if log_type_desc == "ALARM_IN_REMOVED":
            pattern_logs = [{'patterns': ['Alarm removed on the alarm-in port %{NUMBER:numberAlarmInputPort:int}.'],
                             'log_explanation': '某个告警输入接口的告警信号已解除，恢复到正常状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "EDEV_ALARM_IN_REPORTED":
            pattern_logs = [{'patterns': ['Alarm reported on the alarm-in port %{NUMBER:numberAlarmInputPort:int}.'],
                             'log_explanation': '某个告警输入接口收到告警信号',
                             'log_recommended_action': '检查和告警输入接口相连的设备，确认该邻居设备是否发生异常'}]

        elif log_type_desc == "EDEV_BOOTROM_UPDATE_FAILED":
            pattern_logs = [{'patterns': ['Failed to execute the bootrom update command.'],
                             'log_explanation': '用户执行bootrom update命令将文件系统中的BootWare程序加载到BootWare的Normal区，操作失败',
                             'log_recommended_action': '请根据提示信息采取相应措施'}]

        elif log_type_desc == "EDEV_BOOTROM_UPDATE_SUCCESS":
            pattern_logs = [{'patterns': ['Executed the bootrom update command successfully.'],
                             'log_explanation': '用户执行bootrom update命令将文件系统中的BootWare程序加载到BootWare的Normal区，操作成功',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "EDEV_FAILOVER_GROUP_STATE_CHANGE":
            pattern_logs = [{'patterns': [
                'Status of stateful failover group %{DATA:failoverGroupName} with ID %{NUMBER:failoverGroupId:int} changed to  %{DATA:failoverGroupState}.'],
                             'log_explanation': '备份组的状态发生了变化', 'log_recommended_action': '无'}]


    elif module == "EMDI":

        if log_type_desc == "EMDI_INDICATOR_OVER_THRES":
            pattern_logs = [{'patterns': [
                '%{DATA:monitoredItem} alarm for instance %{NUMBER:instanceId:int} was triggered: Value=%{NUMBER:valueMonitoredItem:int}/100000, Threshold=%{NUMBER:alarmThreshold:int}/100000, SuppressionTimes=%{NUMBER:numberConsecutiveAlarmsSuppressedLoggingEvent:int}.'],
                             'log_explanation': 'eMDI监控指标连续多次达到告警阈值',
                             'log_recommended_action': '·          执行display emdi statistics命令，查看实例的统计信息\n·          结合多个设备的实例的统计信息，进行故障定界'}]

        elif log_type_desc == "EMDI_INDICATOR_OVER_THRES_RESUME":
            pattern_logs = [{'patterns': [
                '%{DATA:emidMonitoredItem} alarm for instance %{NUMBER:instanceId:int} was removed: Value=%{NUMBER:valueMonitoredItem:int}/100000, Threshold=%{NUMBER:alarmThreshold:int}/100000, SuppressionTimes=%{NUMBER:numberConsecutiveAlarmsSuppressedLoggingEvent:int}.'],
                             'log_explanation': 'eMDI监控指标连续多次低于告警阈值，监控指标恢复', 'log_recommended_action': '无'}]

        elif log_type_desc == "EMDI_INSTANCE_CONFLICT_FLOW":
            pattern_logs = [{'patterns': [
                'The flow \\(SrcIP=%{DATA:sourceIpAddress}, SrcPort=%{NUMBER:sourcePortNumber:int}, DstIP=%{DATA:destinationIpAddress}, DstPort=%{NUMBER:destinationPortNumber:int}, Protocol=%{DATA:flowType}\\) to be bound to a dynamic instance overlaps with the flow bound to instance %{NUMBER:idEmdiInstanceOverlappingDataFlow:int}.'],
                             'log_explanation': '为动态实例配置的流与已存在实例中的流冲突', 'log_recommended_action': '请删除已存在的冲突配置'}]

        elif log_type_desc == "EMDI_INSTANCE_EXCEED":
            pattern_logs = [{'patterns': [
                'Maximum number of running instances on %{DATA:chassisNumberPlusSlotNumber} already reached.'],
                             'log_explanation': '正在运行的实例已经达到了单板规格最大值',
                             'log_recommended_action': '如果想继续启动一些实例，请先停止一些该板上不必要的实例'}]

        elif log_type_desc == "EMDI_INSTANCE_SAME_FLOW":
            pattern_logs = [{'patterns': [
                'The flow to be bound to a dynamic instance was already bound to instance %{NUMBER:idEmdiInstanceAlreadyBoundDataFlow:int}: SrcIP=%{DATA:sourceIpAddress}, SrcPort=%{NUMBER:sourcePortNumber:int}, DstIP=%{DATA:destinationIpAddress}, DstPort=%{NUMBER:destinationPortNumber:int}, Protocol=%{DATA:flowType}.'],
                             'log_explanation': '为动态实例配置的流与已存在实例中的流相同', 'log_recommended_action': '请删除已存在的冲突配置'}]


    elif module == "ERPS":

        if log_type_desc == "ERPS_STATE_CHANGED":
            pattern_logs = [{'patterns': [
                'Ethernet ring %{NUMBER:erpsRingId:int} instance %{NUMBER:erpsInstanceId:int} changed state to %{DATA:erpsInstanceStatus}.'],
                             'log_explanation': 'ERPS环上实例状态发生改变', 'log_recommended_action': '无'}]


    elif module == "ETH":

        if log_type_desc == "ETH_SET_MAC_FAILED":
            pattern_logs = [{'patterns': ['Failed to set the MAC address %{DATA:macAddress} on %{DATA:interfaceName}.'],
                             'log_explanation': '在配置恢复、IRF分裂、新单板插入情况下，由于接口的MAC地址和设备桥MAC地址的高36位不一致，设置接口的MAC地址失败',
                             'log_recommended_action': '重新配置合适的接口MAC地址'}]


    elif module == "ETHDRNI":

        if log_type_desc == "ETHDRNI_MAC_INEFFECTIVE":
            pattern_logs = [
                {'patterns': ['ETHDRNI failed to add the MAC address of %{DATA:interfaceName}. Cause: %{DATA:cause}.'],
                 'log_explanation': 'ETHDRNI添加VLAN接口的MAC地址失败', 'log_recommended_action': '联系管理员确定操作失败的根因并解决'}]


    elif module == "ETHOAM":

        if log_type_desc == "ETHOAM_CONNECTION_FAIL_DOWN":
            pattern_logs = [{'patterns': [
                'The link is down on interface %{DATA:interfaceName} because a remote failure occurred on peer interface.'],
                             'log_explanation': '对端接口发生故障，链路down', 'log_recommended_action': '检查链路状态或对端的OAM状态'}]

        elif log_type_desc == "ETHOAM_CONNECTION_FAIL_TIMEOUT":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:interfaceName} removed the OAM connection because it received no Information OAMPDU before the timer times out.'],
                             'log_explanation': '接口在超时时间内没有收到信息OAMPDU，所以删除OAM连接',
                             'log_recommended_action': '检查链路状态或对端的OAM状态'}]

        elif log_type_desc == "ETHOAM_CONNECTION_FAIL_UNSATISF":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:interfaceName} failed to establish an OAM connection because the peer doesn’t match the capacity of the local interface.'],
                             'log_explanation': '对端与本端接口的OAM协议状态不匹配，建立OAM连接失败',
                             'log_recommended_action': '分析两端发出的OAM报文中的协议状态字段'}]

        elif log_type_desc == "ETHOAM_CONNECTION_SUCCEED":
            pattern_logs = [{'patterns': ['An OAM connection is established on interface %{DATA:interfaceName}.'],
                             'log_explanation': 'OAM连接建立成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_DISABLE":
            pattern_logs = [{'patterns': ['Ethernet OAM is now disabled on interface %{DATA:interfaceName}.'],
                             'log_explanation': '以太网OAM功能已关闭', 'log_recommended_action': '无'}]

        elif log_type_desc == " ETHOAM_DISCOVERY_EXIT":
            pattern_logs = [{'patterns': ['OAM interface %{DATA:interfaceName} quit the OAM connection..'],
                             'log_explanation': '本端接口退出OAM连接', 'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_ENABLE":
            pattern_logs = [{'patterns': ['Ethernet OAM is now enabled on interface %{DATA:interfaceName}.'],
                             'log_explanation': '以太网OAM功能已使能', 'log_recommended_action': '无'}]

        elif log_type_desc == " ETHOAM_ENTER_LOOPBACK_CTRLLED":
            pattern_logs = [{'patterns': [
                'The local OAM entity enters remote loopback as controlled DTE on OAM interface %{DATA:interfaceName}.'],
                             'log_explanation': '对端使能OAM远端环回功能后，本端OAM实体作为被控制DTE进入远端环回', 'log_recommended_action': '无'}]

        elif log_type_desc == " ETHOAM_ENTER_LOOPBACK_CTRLLING":
            pattern_logs = [{'patterns': [
                'The local OAM entity enters remote loopback as controlling DTE on OAM interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口使能OAM远端环回功能后，本端OAM实体作为控制DTE进入远端环回', 'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_LOCAL_DYING_GASP":
            pattern_logs = [{'patterns': ['A local Dying Gasp event occurred on interface %{DATA:interfaceName}.'],
                             'log_explanation': '重启设备或关闭接口导致本端产生致命故障（Dying Gasp）事件',
                             'log_recommended_action': '链路恢复之前不能使用'}]

        elif log_type_desc == "ETHOAM_LOCAL_ERROR_FRAME":
            pattern_logs = [{'patterns': ['An errored frame event occurred on local interface %{DATA:interfaceName}.'],
                             'log_explanation': '本地接口产生错误帧事件', 'log_recommended_action': '本端收到错误报文，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_LOCAL_ERROR_FRAME_PERIOD":
            pattern_logs = [
                {'patterns': ['An errored frame period event occurred on local interface %{DATA:interfaceName}.'],
                 'log_explanation': '本地接口产生错误帧周期事件', 'log_recommended_action': '本端收到错误报文，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_LOCAL_ERROR_FRAME_SECOND":
            pattern_logs = [{'patterns': ['An errored frame seconds event occurred on local interface %{DATA:param0}.'],
                             'log_explanation': '本地接口产生错误帧秒事件',
                             'log_recommended_action': '本端收到错误报文，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_LOCAL_ERROR_SYMBOL":
            pattern_logs = [{'patterns': ['An errored symbol event occurred on local interface %{DATA:interfaceName}.'],
                             'log_explanation': '本端产生错误信号事件', 'log_recommended_action': '本端收到错误信号，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_LOCAL_LINK_FAULT":
            pattern_logs = [{'patterns': ['A local Link Fault event occurred on interface %{DATA:interfaceName}.'],
                             'log_explanation': '本地链路down，产生链路故障事件', 'log_recommended_action': '重新连接本地接口的光纤接收端'}]

        elif log_type_desc == "ETHOAM_LOOPBACK_EXIT":
            pattern_logs = [{'patterns': ['OAM interface %{DATA:interfaceName} quit remote loopback.'],
                             'log_explanation': '远端环回连接建立未完成时，接口关闭远端环回或OAM连接断开后，OAM接口退出远端环回',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_LOOPBACK_EXIT_ERROR_STATU":
            pattern_logs = [{'patterns': [
                'OAM interface %{DATA:interfaceName} quit remote loopback due to incorrect multiplexer or parser status.'],
                             'log_explanation': '复用器或解析器状态错误，OAM接口Ethernet1/0/1退出远端环回',
                             'log_recommended_action': '在OAM实体上关闭并重新使能以太网OAM'}]

        elif log_type_desc == "ETHOAM_LOOPBACK_NO_RESOURCE":
            pattern_logs = [{'patterns': [
                'OAM interface %{DATA:interfaceName} can’t enter remote loopback due to insufficient resources.'],
                             'log_explanation': '当在本端或对端OAM实体上运行oam remote-loopback start命令时，OAM接口由于资源不足而无法进入远端环回',
                             'log_recommended_action': '端口上使能远端环回，需要设置端口的硬件转发资源，如果配置的端口过多，可能会导致资源不足，需要关闭一下其他端口的远端环回功能，再在本端口上重新运行oam remote-loopback start命令'}]

        elif log_type_desc == "ETHOAM_LOOPBACK_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'OAM interface %{DATA:param0} can’t enter remote loopback because the operation is not supported.'],
                             'log_explanation': '由于设备不支持，OAM接口无法进入远端环回', 'log_recommended_action': '无'}]

        elif log_type_desc == " ETHOAM_NO_ENOUGH_RESOURCE":
            pattern_logs = [{'patterns': [
                'The configuration failed on OAM interface %{DATA:interfaceName} because of insufficient resources.'],
                             'log_explanation': '系统内存资源不足导致OAM接口上的配置失败',
                             'log_recommended_action': '减少一下系统的无用配置，释放部分内存资源后，再重新配置'}]

        elif log_type_desc == " ETHOAM_NOT_CONNECTION_TIMEOUT":
            pattern_logs = [{'patterns': [
                'Interface %{DATA:interfaceName} quit Ethernet OAM because it received no Information OAMPDU before the timer times out.'],
                             'log_explanation': '本地端口在超时时间内没有收到信息OAMPDU，所以退出以太网OAM',
                             'log_recommended_action': '对端发送OAM报文不及时，检查本地和对端的链路状态是否正常，以及对端的OAM功能是否使能了'}]

        elif log_type_desc == " ETHOAM_QUIT_LOOPBACK_CTRLLED":
            pattern_logs = [{'patterns': [
                'The local OAM entity quit remote loopback as controlled DTE on OAM interface %{DATA:interfaceName}.'],
                             'log_explanation': '当本端作为远端环回的被控端时，由于对端关闭了远端环回功能，本端也会退出远端环回',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_QUIT_LOOPBACK_CONTROLLING":
            pattern_logs = [{'patterns': [
                'The local OAM entity quit remote loopback as controlling DTE on OAM interface %{DATA:interfaceName}.'],
                             'log_explanation': '在接口上使能远端环回，当再将端口上的远端环回功能关闭后，本端会退出远端环回', 'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_REMOTE_CRITICAL":
            pattern_logs = [{'patterns': ['A remote Critical event occurred on interface %{DATA:interfaceName}.'],
                             'log_explanation': '发生远端紧急事件', 'log_recommended_action': '链路恢复之前不能使用'}]

        elif log_type_desc == "ETHOAM_REMOTE_DYING_GASP":
            pattern_logs = [{'patterns': ['A remote Dying Gasp event occurred on interface %{DATA:interfaceName}.'],
                             'log_explanation': '重启远端设备或关闭接口导致远端产生致命故障（Dying Gasp）事件',
                             'log_recommended_action': '链路恢复之前不能使用'}]

        elif log_type_desc == "ETHOAM_REMOTE_ERROR_FRAME":
            pattern_logs = [
                {'patterns': ['An errored frame event occurred on the peer interface %{DATA:interfaceName}.'],
                 'log_explanation': '对端产生错误帧事件', 'log_recommended_action': '对端收到错误报文，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_REMOTE_ERROR_FRAME_PERIOD":
            pattern_logs = [
                {'patterns': ['An errored frame period event occurred on the peer interface %{DATA:interfaceName}.'],
                 'log_explanation': '对端产生错误帧周期事件', 'log_recommended_action': '对端收到错误报文，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_REMOTE_ERROR_FRAME_SECOND":
            pattern_logs = [
                {'patterns': ['An errored frame seconds event occurred on the peer interface %{DATA:interfaceName}.'],
                 'log_explanation': '对端产生错误帧秒事件', 'log_recommended_action': '对端收到错误报文，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == "ETHOAM_REMOTE_ERROR_SYMBOL":
            pattern_logs = [
                {'patterns': ['An errored symbol event occurred on the peer interface %{DATA:interfaceName}.'],
                 'log_explanation': '对端产生错误信号事件', 'log_recommended_action': '对端收到错误信号，检查一下本端和对端之间的链路是否正常'}]

        elif log_type_desc == " ETHOAM_REMOTE_EXIT":
            pattern_logs = [{'patterns': [
                'OAM interface %{DATA:interfaceName} quit OAM connection because Ethernet OAM is disabled on the peer interface.'],
                             'log_explanation': '对端接口关闭以太网OAM功能导致本端接口退出OAM连接', 'log_recommended_action': '无'}]

        elif log_type_desc == " ETHOAM_REMOTE_FAILURE_RECOVER":
            pattern_logs = [{'patterns': ['Peer interface %{DATA:interfaceName} recovered.'],
                             'log_explanation': '对端接口链路故障清除，OAM连接恢复', 'log_recommended_action': '无'}]

        elif log_type_desc == "ETHOAM_REMOTE_LINK_FAULT":
            pattern_logs = [{'patterns': ['A remote Link Fault event occurred on interface %{DATA:interfaceName}.'],
                             'log_explanation': '远端链路down，产生远端链路故障事件', 'log_recommended_action': '重新连接远端接口的光纤接收端'}]


    elif module == "EVB":

        if log_type_desc == "EVB_AGG_FAILED":
            pattern_logs = [{'patterns': [
                'Remove port %{DATA:portName} from aggregation group %{DATA:aggregateInterfaceName}. Otherwise, the EVB feature does not take effect.'],
                             'log_explanation': 'EVB交换机处理聚合组中物理接口失败', 'log_recommended_action': '将该物理接口从聚合组中删除'}]

        elif log_type_desc == "EVB_LICENSE_EXPIRE":
            pattern_logs = [{'patterns': ["The EVB feature's license will expire in %{NUMBER:numberDays:int} days."],
                             'log_explanation': 'EVB的License将在指定天数后失效', 'log_recommended_action': '更新EVB的License'}]

        elif log_type_desc == "EVB_VSI_OFFLINE":
            pattern_logs = [{'patterns': ['VSI %{DATA:vsiInterface/vsiAggregateInterfaceName} went offline.'],
                             'log_explanation': '设备收到服务器发送的VDP报文，或者定时器已经超时，但设备还没收到服务器的VDP回复报文，VSI接口/VSI聚合接口被删除',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "EVB_VSI_ONLINE":
            pattern_logs = [{'patterns': [
                'VSI %{DATA:vsiInterface/vsiAggregateInterfaceName} came online, status is %{DATA:vsiStatus}.'],
                             'log_explanation': 'EVB交换机收到VDP报文并成功创建VSI接口/VSI聚合接口', 'log_recommended_action': '无'}]


    elif module == "EVIISIS":

        if log_type_desc == "EVIISIS_LICENSE_EXPIRED":
            pattern_logs = [{'patterns': ['The EVIISIS feature is being disabled, because its license has expired.'],
                             'log_explanation': 'EVIISIS的License已经过期', 'log_recommended_action': '请更换有效的Licence'}]

        elif log_type_desc == "EVIISIS_LICENSE_EXPIRED_TIME":
            pattern_logs = [
                {'patterns': ['The EVIISIS feature will be disabled in %{NUMBER:availablePeriodFeature:int} days.'],
                 'log_explanation': 'EVIISIS的License不可用，EVIISIS功能将在2天后失效\n\n主备倒换后新的主控板上没有可用的EVI License，会启动30天临时可用定时器',
                 'log_recommended_action': '若要继续使用EVIISIS功能，请准备新的License'}]

        elif log_type_desc == "EVIISIS_LICENSE_UNAVAILABLE":
            pattern_logs = [{'patterns': ['The EVIISIS feature has no available license.'],
                             'log_explanation': '进程启动时，没有找到EVIISIS对应的License',
                             'log_recommended_action': '请为EVIISIS安装有效的Licence'}]

        elif log_type_desc == "EVIISIS_NBR_CHG":
            pattern_logs = [{'patterns': [
                'EVIISIS %{NUMBER:param0:int}, %{DATA:param1} adjacency %{DATA:param2} \\(%{DATA:param3}\\), state changed to %{DATA:param4}.'],
                             'log_explanation': '接口EVI IS-IS邻居状态改变',
                             'log_recommended_action': '当某接口邻居状态变为down或initializing时，检查EVI IS-IS配置正确性和网络连通性'}]


    elif module == "FCLINK":

        if log_type_desc == "FCLINK_FDISC_REJECT_NORESOURCE":
            pattern_logs = [{'patterns': [
                'VSAN %{NUMBER:vsanId:int}, Interface %{DATA:interfaceName}: An FDISC was rejected because the hardware resource is not enough.'],
                             'log_explanation': '硬件资源不足时收到了FDISC报文', 'log_recommended_action': '减少节点的数量'}]

        elif log_type_desc == "FCLINK_FLOGI_REJECT_NORESOURCE":
            pattern_logs = [{'patterns': [
                'VSAN %{NUMBER:vsanId:int}, Interface %{DATA:interfaceName}: An FLOGI was rejected because the hardware resource is not enough.'],
                             'log_explanation': '硬件资源不足时收到了FLOGI报文', 'log_recommended_action': '减少节点的数量'}]


    elif module == "FCOE":

        if log_type_desc == "FCOE_LAGG_BIND_ACTIVE":
            pattern_logs = [{'patterns': [
                'The binding between aggregate interface %{DATA:aggregateInterfaceName} and the VFC interface takes effect again, because the member port is unbound from its bound VFC interface or removed from the aggregate interface.'],
                             'log_explanation': '因为聚合接口的成员接口解除VFC接口绑定或退出聚合组，所以聚合接口绑定的VFC接口生效',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "FCOE_LAGG_BIND_DEACTIVE":
            pattern_logs = [{'patterns': [
                'The binding between aggregate interface %{DATA:aggregateInterfaceName} and the VFC interface is no longer in effect, because the new member port has been bound to a VFC interface.'],
                             'log_explanation': '因为聚合接口的成员口绑定了VFC接口，所以聚合接口绑定的VFC接口失效', 'log_recommended_action': '无'}]

        elif log_type_desc == "FCOE_INTERFACE_NOTSUPPORT_FCOE":
            pattern_logs = [{'patterns': [
                'Because the aggregate interface %{DATA:aggregateInterfaceName} has been bound to a VFC interface, assigning the interface %{DATA:ethernetInterfaceName} that does not support FCoE to the aggregate interface might cause incorrect processing.'],
                             'log_explanation': '当不支持FCoE功能的接口加入到已绑定到VFC接口的聚合接口时，打印本信息',
                             'log_recommended_action': '将支持FCoE功能的接口加入到聚合接口，或者解除聚合接口与VFC接口的绑定'}]


    elif module == "FCZONE":

        if log_type_desc == "FCZONE_DISTRIBUTE_FAILED":
            pattern_logs = [{'patterns': [
                'Zone distribution failed. The zoning configurations might consequently be inconsistent across the fabric.'],
                             'log_explanation': '扩散失败，Fabric中交换机的zone配置可能因此不一致',
                             'log_recommended_action': '不同情况下扩散失败的处理建议如下：\n·          如果是激活Zone set命令zoneset activate触发的扩散，需要分别在Fabric中各交换机上通过display current-configuration命令查看VSAN内的激活Zone set的配置，若配置不一致，则通过zoneset activate命令重新激活该Zone set，以保证Fabric内所有交换机的激活Zone set的数据一致性\n·          如果是完全扩散命令zoneset distribute触发的扩散，需要分别在Fabric中各交换机上通过display current-configuration命令查看VSAN内的激活Zone set和Zone数据库配置，若配置不一致，则通过zoneset distribute命令重新激发一次完全扩散，以保证Fabric内所有交换机的Zone配置的一致性\n·          如果是Zone模式切换触发的扩散，需要分别在Fabric中各交换机上通过display zone status命令查看VSAN内的Zone模式，如果各交换机的Zone模式不一致，则通过zoneset distribute命令来主动激发一次完全扩散，以保证Fabric内所有交换机的Zone模式的一致性'}]

        elif log_type_desc == "FCZONE_HARDZONE_DISABLED":
            pattern_logs = [{'patterns': ['No enough hardware resource for zone rule, switched to soft zoning.'],
                             'log_explanation': '硬件资源不足', 'log_recommended_action': '激活一个更小的zone set'}]

        elif log_type_desc == "FCZONE_HARDZONE_ENABLED":
            pattern_logs = [{'patterns': ['Hardware resource for zone rule is restored, switched to hard zoning.'],
                             'log_explanation': '硬件资源恢复时，切换到hard zoning', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "FCZONE_ISOLATE_ALLNEIGHBOR":
            pattern_logs = [{'patterns': [
                'The E ports connected to all neighbors were isolated, because the length of the locally generated MR packet exceeded the limit.'],
                             'log_explanation': '因本地生成的MR报文长度超限，隔离与所有邻居相连的E-Port',
                             'log_recommended_action': '通过display current-configuration命令查看本地交换机VSAN内的Zone配置，删除Zone set中不必要的配置，或重新激活一个较小的Zone set。然后，对因MR报文超大导致隔离的E-Port配置shutdown和undo shutdown命令，触发重新发起合并'}]

        elif log_type_desc == "FCZONE_ISOLATE_CLEAR_ALLVSAN":
            pattern_logs = [{'patterns': ['Isolation status was cleared in all supported VSANs.'],
                             'log_explanation': '接口在所有支持的VSAN内去隔离', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "FCZONE_ISOLATE_CLEAR_VSAN":
            pattern_logs = [{'patterns': ['Isolation status was cleared.'], 'log_explanation': '接口在指定VSAN内去隔离',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "FCZONE_ISOLATE_NEIGHBOR":
            pattern_logs = [{'patterns': [
                "All the E ports connected to a neighbor were isolated because of merge failure, and the neighbor’s switch WWN is %{DATA:neighbor'sSwitchWwn}."],
                             'log_explanation': '因与邻居交换机合并失败，隔离与该邻居相连的所有E-Port',
                             'log_recommended_action': '分别在本地和邻居交换机上通过display current-configuration命令查看VSAN内的Zone配置，并修改配置使其符合合并规则。然后，对因合并失败导致隔离的E-Port配置shutdown和undo shutdown命令触发两台交换机重新发起合并'}]


    elif module == "FGROUP":

        if log_type_desc == "FLOWGROUP_APPLY_FAIL":
            pattern_logs = [
                {'patterns': ['Failed to apply flow group %{DATA:flowGroupId}. Reason: %{DATA:failureCause}'],
                 'log_explanation': '·          不支持配置，导致应用Flow Group失败\n·          资源不足，导致应用Flow Group失败',
                 'log_recommended_action': '请根据失败原因，修改或删除Flow Group的相关配置'}]

        elif log_type_desc == "FLOWGROUP_MODIFY_FAIL":
            pattern_logs = [
                {'patterns': ['Failed to modify flow group %{DATA:flowGroupId}. Reason: %{DATA:failureCause}'],
                 'log_explanation': '·          不支持配置，导致修改Flow Group失败\n·          资源不足，导致修改Flow Group失败',
                 'log_recommended_action': '如果是资源不足导致修改失败，请检查并删除设备上不必要的配置，以节约资源'}]


    elif module == "FIB":

        if log_type_desc == "FIB_FILE":
            pattern_logs = [{'patterns': ['Failed to save the IP forwarding table due to lack of storage resources.'],
                             'log_explanation': '存储介质剩余空间不足，保存IP FIB信息失败',
                             'log_recommended_action': '删除其它无用文件，释放存储介质的存储空间'}]


    elif module == "FILTER":

        if log_type_desc == "FILTER_EXECUTION_ICMP":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:param0};Direction\\(1070\\)=%{DATA:param1};AclType\\(1067\\)=%{DATA:param2};Acl\\(1068\\)=%{DATA:param3};Protocol\\(1001\\)=%{DATA:param4};SrcIPAddr\\(1003\\)=%{IP:param5};DstIPAddr\\(1007\\)=%{IP:param6};IcmpType\\(1062\\)=%{DATA:param7}\\(%{NUMBER:param8:int}\\);IcmpCode\\(1063\\)=%{NUMBER:param9:int};MatchAclCount\\(1069\\)=%{NUMBER:param10:int};Event\\(1048\\)=%{DATA:param11};'],
                             'log_explanation': '首次命中包过滤时发送ICMP报文过滤日志，之后定时发送该日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "FILTER_EXECUTION_ICMPV6":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:param0};Direction\\(1070\\)=%{DATA:param1};AclType\\(1067\\)=%{DATA:param2};Acl\\(1068\\)=%{DATA:param3};Protocol\\(1001\\)=%{DATA:param4};SrcIPv6Addr\\(1036\\)=%{IP:param5};DstIPv6Addr\\(1037\\)=%{IP:param6};Icmpv6Type\\(1064\\)=%{DATA:param7}\\(%{NUMBER:param8:int}\\);Icmpv6Code\\(1065\\)=%{NUMBER:param9:int};MatchAclCount\\(1069\\)=%{NUMBER:param10:int};Event\\(1048\\)=%{DATA:param11};'],
                             'log_explanation': '首次命中包过滤时发送ICMPV6报文过滤日志，之后定时发送该日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "FILTER_IPV4_EXECUTION":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName};Direction\\(1070\\)=%{DATA:direction};AclType\\(1067\\)=%{DATA:aclType};Acl\\(1068\\)=%{DATA:aclNumberName};Protocol\\(1001\\)=%{DATA:layer4ProtocolName};SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress};SrcPort\\(1004\\)=%{NUMBER:sourcePort:int};DstIPAddr\\(1007\\)=%{IP:destinationIpAddress};DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int};MatchAclCount\\(1069\\)=%{NUMBER:matchCount:int};Event\\(1048\\)=%{DATA:eventInformation};'],
                             'log_explanation': '首次命中包过滤时发送报文过滤日志，之后定时发送该日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "FILTER_IPV6_EXECUTION":
            pattern_logs = [{'patterns': [
                'RcvIfName\\(1023\\)=%{DATA:receivingInterfaceName};Direction\\(1070\\)=%{DATA:direction};AclType\\(1067\\)=%{DATA:aclType};Acl\\(1068\\)=%{DATA:aclNumberName};Protocol\\(1001\\)=%{DATA:layer4ProtocolName};SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address};SrcPort\\(1004\\)=%{NUMBER:sourcePortNumber:int};DstIPv6Addr\\(1037\\)=%{IP:destinationIpv6Address};DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int};MatchAclCount\\(1069\\)=%{NUMBER:matchCount:int};Event\\(1048\\)=%{DATA:eventInformation};'],
                             'log_explanation': '首次命中包过滤时发送报文过滤日志，之后定时发送该日志', 'log_recommended_action': '无'}]


    elif module == "FIPSNG":

        if log_type_desc == "FIPSNG_HARD_RESOURCE_NOENOUGH":
            pattern_logs = [
                {'patterns': ['No enough hardware resource for FIP snooping rule.'], 'log_explanation': '硬件资源不足',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "FIPSNG_HARD_RESOURCE_RESTORE":
            pattern_logs = [
                {'patterns': ['Hardware resource for FIP snooping rule is restored.'], 'log_explanation': '硬件资源恢复',
                 'log_recommended_action': '无'}]


    elif module == "FS":

        if log_type_desc == "FS_UNFORMATED_PARTITION":
            pattern_logs = [
                {'patterns': ['Partition %{DATA:param0} is not formatted yet. Please format the partition first.'],
                 'log_explanation': '分区未格式化，请先执行格式化操作', 'log_recommended_action': '格式化该分区'}]


    elif module == "FTP":

        if log_type_desc == "FTP_ACL_DENY":
            pattern_logs = [{'patterns': [
                'The FTP Connection %{IP:ipAddressFtpClient}\\(%{DATA:vpnInstanceIpAddressFtpClientBelongs}\\) request was denied according to ACL rules.'],
                             'log_explanation': 'FTP ACL规则限制登录IP地址。该日志在FTP服务端检测到非法客户端尝试登录时输出',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "FTPD_AUTHOR_FAILED":
            pattern_logs = [{'patterns': ['Authorization failed for user %{DATA:username}@%{DATA:ipAddressFtpClient}.'],
                             'log_explanation': 'FTP用户授权失败', 'log_recommended_action': '请检查是否配置该用户支持FTP服务'}]

        elif log_type_desc == "FTP_REACH_SESSION_LIMIT":
            pattern_logs = [{'patterns': [
                'FTP client %{DATA:ipAddressFtpClient} failed to log in. The current number of FTP sessions is %{NUMBER:currentNumberFtpSessions:int}. The maximum number allowed is \\(%{NUMBER:maximumNumberFtpSessionsAllowedDevice:int}\\).'],
                             'log_explanation': 'FTP登录用户达到上限。该日志在FTP服务端检测到登录客户端数达到上限时输出',
                             'log_recommended_action': '·          请使用display current-configuration | include sesion-limit命令查看设备当前允许的FTP最大登录用户数（如果执行该display命令后没有显示，则表示使用的是缺省配置）\n·          根据需要使用aaa session-limit命令配置允许的FTP最大登录用户数'}]


    elif module == "GRPC":

        if log_type_desc == "GRPC_LOGIN":
            pattern_logs = [
                {'patterns': ['%{DATA:username} logged in from %{DATA:clientId}, session id %{NUMBER:sessionId:int}.'],
                 'log_explanation': '用户登录成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "GRPC_LOGIN_FAILED":
            pattern_logs = [{'patterns': ['%{DATA:param0} from %{DATA:param1} login failed.',
                                          '%{DATA:param2} from %{DATA:param3} login failed. %{DATA:param4}'],
                             'log_explanation': '用户登录失败',
                             'log_recommended_action': '1.      如果未显示失败原因，请检查是否已配置用户，以及用户名和密码是否正确\n2.      如果显示gRPC会话到达数量上限，请减少gRPC客户端连接数'}]

        elif log_type_desc == "GRPC_LOGOUT":
            pattern_logs = [{'patterns': ['%{DATA:username} logged out, session id %{NUMBER:sessionId:int}.'],
                             'log_explanation': '用户正常登出', 'log_recommended_action': '无'}]

        elif log_type_desc == "GRPC_SERVER_FAILED":
            pattern_logs = [{'patterns': ['Failed to enable gRPC server.'], 'log_explanation': '因端口冲突，无法和gRPC服务器建立连接',
                             'log_recommended_action': '检查是否端口号被占用'}]

        elif log_type_desc == "GRPC_SUBSCRIBE_EVENT_FAILED":
            pattern_logs = [{'patterns': ['Failed to subscribe event %{DATA:param0}.'], 'log_explanation': '订阅事件失败',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "GRPC_RECEIVE_SUBSCRIPTION":
            pattern_logs = [
                {'patterns': ['Received a subscription of module %{DATA:param0}.'], 'log_explanation': '收到某个模块的一个订阅事件',
                 'log_recommended_action': '无'}]


    elif module == "HA":

        if log_type_desc == "HA_BATCHBACKUP_FINISHED":
            pattern_logs = [{'patterns': [
                'Batch backup of standby board in %{DATA:chassisNumberSlotNumberSlotNumber} has finished.'],
                             'log_explanation': '主用主控板和备用主控板之间的批量备份完成', 'log_recommended_action': '无'}]

        elif log_type_desc == "HA_BATCHBACKUP_STARTED":
            pattern_logs = [
                {'patterns': ['Batch backup of standby board in %{DATA:chassisNumberSlotNumberSlotNumber} started.'],
                 'log_explanation': '主用主控板和备用主控板之间的批量备份开始', 'log_recommended_action': '无'}]

        elif log_type_desc == "HA_STANDBY_NOT_READY":
            pattern_logs = [
                {'patterns': ['Standby board in %{DATA:chassisNumberSlotNumberSlotNumber} is not ready, reboot ...'],
                 'log_explanation': '主备倒换时，如果备用主控板未准备好，则不会进行主备倒换，而是重启备用主控板和主用主控板，并在备用主控板上打印该信息',
                 'log_recommended_action': '建议备用主控板批量备份完成前不要进行主备倒换'}]

        elif log_type_desc == "HA_STANDBY_TO_MASTER":
            pattern_logs = [
                {'patterns': ['Standby board in %{DATA:chassisNumberSlotNumberSlotNumber} changed to the master.'],
                 'log_explanation': '发生主备倒换，备用主控板成为主用主控板', 'log_recommended_action': '无'}]


    elif module == "HLTH":

        if log_type_desc == "LIPC_COMM_FAULTY":
            pattern_logs = [{'patterns': [
                'LIPC %{DATA:lipcCommunicationType} between %{DATA:chassisNumberSlotNumberCpuNumber} and %{DATA:chassisNumberSlotNumberCpuNumber} might be faulty.'],
                             'log_explanation': 'LIPC通信异常',
                             'log_recommended_action': '使用display system health命令查看设备的健康状态，如果30分钟后设备仍处于故障状态，请联系技术支持'}]

        elif log_type_desc == "LIPC_COMM_NORMAL":
            pattern_logs = [{'patterns': [
                'LIPC %{DATA:lipcCommunicationType} between %{DATA:chassisNumberSlotNumberCpuNumber} and %{DATA:chassisNumberSlotNumberCpuNumber} recovered.'],
                             'log_explanation': 'LIPC通信恢复正常', 'log_recommended_action': '无'}]


    elif module == "HQOS":

        if log_type_desc == "HQOS_DP_SET_FAIL":
            pattern_logs = [{'patterns': ['Failed to set drop profile %{DATA:dropProfileName} globally.'],
                             'log_explanation': '首次应用全局丢弃策略或者修改全局丢弃策略时失败',
                             'log_recommended_action': '请检查丢弃策略配置，确保支持并且策略不冲突'}]

        elif log_type_desc == "HQOS_FP_SET_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to set %{DATA:policyType} in forwarding profile %{DATA:forwardingProfileName} globally.'],
                             'log_explanation': '首次应用全局转发策略或者修改全局转发策略时失败',
                             'log_recommended_action': '请检查转发策略，确保支持并且策略不冲突'}]

        elif log_type_desc == "HQOS_POLICY_APPLY_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply some forwarding classes or forwarding groups in scheduler policy %{DATA:schedulerPolicyName} to the %{DATA:policyDirection} direction of interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口上应用调度策略失败，或者修改接口上已应用的调度策略',
                             'log_recommended_action': '通过命令行display qos scheduler-policy diagnosis interface查看失败的转发节点以及失败原因，之后检查运行配置'}]

        elif log_type_desc == "HQOS_POLICY_RECOVER_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to recover scheduler policy %{DATA:schedulerPolicyName} to the %{DATA:policyDirection} direction of interface %{DATA:interfaceName} due to %{DATA:cause}.'],
                             'log_explanation': '接口板重启或设备重启，恢复接口上应用的调度策略失败', 'log_recommended_action': '请根据失败原因检查配置'}]


    elif module == "HTTPD":

        if log_type_desc == "HTTPD_CONNECT":
            pattern_logs = [{'patterns': [
                '%{DATA:connectionType} client %{DATA:clientIpAddress} connected to the server successfully.'],
                             'log_explanation': 'HTTP/HTTPS服务器接受了客户端的请求，HTTP/HTTPS连接成功建立',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "HTTPD_CONNECT_TIMEOUT":
            pattern_logs = [
                {'patterns': ['%{DATA:connectionType} client %{DATA:clientIpAddress} connection idle timeout.'],
                 'log_explanation': 'HTTP/HTTPS连接因空闲时间太长而断开', 'log_recommended_action': '无'}]

        elif log_type_desc == "HTTPD_DISCONNECT":
            pattern_logs = [
                {'patterns': ['%{DATA:connectionType} client %{DATA:clientIpAddress} disconnected from the server.'],
                 'log_explanation': 'HTTP/HTTPS 客户端断开了到服务器的连接', 'log_recommended_action': '无'}]

        elif log_type_desc == "HTTPD_FAIL_FOR_ACL":
            pattern_logs = [{'patterns': [
                '%{DATA:connectionType} client %{DATA:clientIpAddress} failed the ACL check and could not connect to the server.'],
                             'log_explanation': 'HTTP/HTTPS客户端没有通过ACL检查，无法建立连接', 'log_recommended_action': '无'}]

        elif log_type_desc == "HTTPD_FAIL_FOR_ACP":
            pattern_logs = [{'patterns': [
                '%{DATA:connectionType} client %{DATA:clientIpAddress} was denied by the certificate access control policy and could not connect to the server.'],
                             'log_explanation': 'HTTP/HTTPS客户端没有通过证书接入控制策略检查，无法建立连接', 'log_recommended_action': '无'}]

        elif log_type_desc == "HTTPD_REACH_CONNECT_LIMIT":
            pattern_logs = [{'patterns': [
                '%{DATA:connectionType} client %{DATA:clientIpAddress} failed to connect to the server, because the number of connections reached the upper limit.'],
                             'log_explanation': '已达到最大连接数，无法建立新的连接',
                             'log_recommended_action': '请根据需要使用命令aaa session-limit配置允许的Web最大登录用户数'}]


    elif module == "IFNET":

        if log_type_desc == "IF_JUMBOFRAME_WARN":
            pattern_logs = [{'patterns': [
                'The specified size of jumbo frames on the aggregate interface %{DATA:aggregateInterfaceName} is not supported on the member port %{DATA:memberPortName}.'],
                             'log_explanation': '聚合接口修改jumboframe enable [ size ]配置，部分成员端口不支持',
                             'log_recommended_action': '确认成员端口支持配置的size范围，将聚合接口的size配置在该范围内'}]

        elif log_type_desc == "IF_BUFFER_CONGESTION_CLEAR":
            pattern_logs = [{'patterns': [
                '%{DATA:dataBufferType} congestion on queue %{NUMBER:queueIdRange07:int} of %{DATA:interfaceName} is cleared. %{NUMBER:numberPacketsDropped:int} packets are discarded.'],
                             'log_explanation': '在接口GigabitEthernet1/0/1上队列1接收数据缓冲区的拥塞解除。共有1000个报文被丢弃',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "IF_BUFFER_CONGESTION_OCCURRENCE":
            pattern_logs = [{'patterns': [
                '%{DATA:dataBufferType} congestion occurs on queue %{NUMBER:queueIdRange07:int} of %{DATA:interfaceName}.'],
                             'log_explanation': '在接口GigabitEthernet1/0/1上队列1的接收数据缓冲区发生拥塞',
                             'log_recommended_action': '检查网络状况'}]

        elif log_type_desc == "IF_LINKFLAP_DETECTED":
            pattern_logs = [{'patterns': ['Link flapping was detected on %{DATA:interfaceName}.'],
                             'log_explanation': '在链路震荡检查时间间隔内，接口状态从UP变为DOWN的次数大于等于链路震荡次数阈值',
                             'log_recommended_action': '1.      检查接口（本端或对端）连线是否被频繁插拔\n2.      通过port link-flap protect enable命令调整链路震荡检查时间间隔和链路震荡次数阈值'}]

        elif log_type_desc == "INTERFACE_NOTSUPPRESSED":
            pattern_logs = [{'patterns': ['Interface %{DATA:interfaceName} is not suppressed.'],
                             'log_explanation': '接口由抑制状态变为非抑制状态，此时上层业务可以感知接口UP/DOWN状态变化',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "INTERFACE_SUPPRESSED":
            pattern_logs = [{'patterns': ['Interface %{DATA:interfaceName} was suppressed.'],
                             'log_explanation': '当接口状态频繁变化时，接口被抑制。抑制期间，上层业务不能感知端口UP/DOWN状态变化',
                             'log_recommended_action': '3.      检查接口（本端或对端）连线是否被频繁插拔\n4.      通过配置以太网接口物理连接状态抑制功能调整抑制参数'}]

        elif log_type_desc == "TUNNEL_LINK_UPDOWN":
            pattern_logs = [{'patterns': [
                'Line protocol state on the interface %{DATA:interfaceName} changed to %{DATA:protocolState}.'],
                             'log_explanation': 'Tunnel接口的链路层协议状态发生变化',
                             'log_recommended_action': '链路层状态为down时，请使用display interface命令查看链路层状态，进一步定位链路层状态为down的原因'}]

        elif log_type_desc == "TUNNEL_PHY_UPDOWN":
            pattern_logs = [{'patterns': [
                'Physical state on the interface %{DATA:interfaceName} changed to %{DATA:protocolState}.'],
                             'log_explanation': 'Tunnel接口的链路状态发生变化',
                             'log_recommended_action': '物理层状态为down时，请检查是否没有物理连线或者链路故障'}]

        elif log_type_desc == "PROTOCOL_UPDOWN":
            pattern_logs = [{'patterns': [
                'Protocol %{DATA:protocolName} state on the interface %{DATA:interfaceName} changed to %{DATA:protocolState}.'],
                             'log_explanation': '接口上一个协议的状态发生变化', 'log_recommended_action': '网络层状态为down时，请检查网络层协议配置'}]

        elif log_type_desc == "VLAN_MODE_CHANGE":
            pattern_logs = [{'patterns': ['Dynamic VLAN %{NUMBER:vlanId:int} has changed to a static VLAN.'],
                             'log_explanation': '创建VLAN接口导致动态VLAN转换成静态VLAN', 'log_recommended_action': '无'}]


    elif module == "IKE":

        if log_type_desc == "IKE_P1_SA_ESTABLISH_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to establish phase 1 SA for the reason of %{DATA:reasonFailure}. The SA’s source address is %{DATA:sourceAddress}, and its destination address is %{DATA:destinationAddress}.'],
                             'log_explanation': 'IKE建立第一阶段SA失败以及失败原因', 'log_recommended_action': '检查本端和对端设备的IKE配置'}]

        elif log_type_desc == "IKE_P2_SA_ESTABLISH_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to establish phase 2 SA for the reason of %{DATA:reasonFailure}. The SA’s source address is %{DATA:sourceAddress}, and its destination address is %{DATA:destinationAddress}.'],
                             'log_explanation': 'IKE建立第二阶段SA失败以及失败原因',
                             'log_recommended_action': '检查本端和对端设备的IKE和IPsec配置'}]

        elif log_type_desc == "IKE_P2_SA_TERMINATE":
            pattern_logs = [{'patterns': [
                'The IKE phase 2 SA was deleted for the reason of %{DATA:reasonSaDeleted}. The SA’s source address is %{DATA:sourceAddress}, and its destination address is %{DATA:destinationAddress}.'],
                             'log_explanation': '第二阶段SA由于过期失效而删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "IKE_VERIFY_CERT_FAIL":
            pattern_logs = [{'patterns': ['Failed to verify the peer certificate. Reason: %{DATA:failureReason}.'],
                             'log_explanation': '验证证书失败，可能原因，证书格式无效等', 'log_recommended_action': '无'}]


    elif module == "IMA":

        if log_type_desc == "IMA_ALLOCATE_FAILED":
            pattern_logs = [{'patterns': ['Failed to allocate resource for file %{DATA:nameFileWantMeasureIntegrity}.'],
                             'log_explanation': 'IMA给度量目标文件分配资源失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "IMA_DATA_ERROR":
            pattern_logs = [{'patterns': ["Can't collect data of file %{DATA:nameFileWantMeasureIntegrity}."],
                             'log_explanation': '收集目标文件的数据失败，可能是打开或读取文件失败，或计算文件Hash值出错',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "IMA_RM_FILE_MISS":
            pattern_logs = [{'patterns': ['File %{DATA:nameFileWantMeasureIntegrity} is missing in the RM file.'],
                             'log_explanation': 'RM文件中未找到目标文件的信息', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "IMA_RM_HASH_MISS":
            pattern_logs = [
                {'patterns': ['Hash value of file %{DATA:nameFileWantMeasureIntegrity} is missing in the RM file.'],
                 'log_explanation': 'RM文件中没有目标文件的Hash值，可能目标文件在度量时使用的Hash算法在RM中不支持',
                 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "IMA_TEMPLATE_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to extend template hash value of file %{DATA:nameFileWantMeasureIntegrity} to the PCR.'],
                             'log_explanation': '将目标文件的模板Hash值扩展到PCR失败', 'log_recommended_action': '请联系技术支持'}]


    elif module == "PTS":

        if log_type_desc == "PTS_FILE_HASH_FAILED":
            pattern_logs = [{'patterns': [
                'Hash value of file %{DATA:nameFileWantMeasureIntegrity} is not consistent with that in the RM file.'],
                             'log_explanation': '目标文件的HASH值与RM文件中该文件的HASH值不匹配，此时该文件不可信',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_AK_AUTH_FAILED":
            pattern_logs = [{'patterns': ['Inconsistent authorization data for attestation key %{DATA:akName}.'],
                             'log_explanation': 'AK密钥对应的授权数据错误',
                             'log_recommended_action': '配置可信报告使用的AK密钥时使用的授权数据需要和创建该密钥时配置的授权数据一致（相关命令为key create）'}]

        elif log_type_desc == "PTS_AK_INVALID":
            pattern_logs = [
                {'patterns': ['The attestation key %{DATA:akName} is incorrect.'], 'log_explanation': 'AK密钥无效',
                 'log_recommended_action': '重新配置可信报告使用的AK密钥'}]

        elif log_type_desc == "PTS_AK_NO_CERT":
            pattern_logs = [{'patterns': ['No certificate file found for attestation key %{DATA:akName}.'],
                             'log_explanation': 'AK密钥缺少证书', 'log_recommended_action': '通过管理端为设备的AK密钥签发AK证书'}]

        elif log_type_desc == "PTS_AK_NO_EXIST":
            pattern_logs = [
                {'patterns': ["Attestation key %{DATA:akName} doesn't exist."], 'log_explanation': '指定名称的AK密钥不存在',
                 'log_recommended_action': '配置AK密钥（相关命令为key create）'}]

        elif log_type_desc == "PTS_AK_NO_LOAD":
            pattern_logs = [
                {'patterns': ['The attestation key %{DATA:akName} is not loaded.'], 'log_explanation': 'AK密钥未加载到安全芯片',
                 'log_recommended_action': '通过key load命令将AK密钥加载到可信计算芯片'}]

        elif log_type_desc == "PTS_BTW_PCR_FAILED":
            pattern_logs = [{'patterns': [
                'Hash value computed based on BootWare IML is not consistent with that in PCR \\(%{NUMBER:pcrIndex:int}\\).'],
                             'log_explanation': '使用BootWare可信度量日志计算出来的HASH值与保存在PCR中的HASH值不同，此时BootWare程序不可信',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_CHECK_RM_VERSION_FAILED":
            pattern_logs = [{'patterns': ['Version the RM file %{DATA:rmFileName} is not supported.'],
                             'log_explanation': '设备不支持当前RM文件版本', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_AGED_TIMER_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to create PTS session ageing timer.'], 'log_explanation': '创建PTS会话老化定时器失败',
                 'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_CHECK_TIMER_FAILED":
            pattern_logs = [{'patterns': ['Failed to create server check timer.'], 'log_explanation': '创建Server检查定时器失败',
                             'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_CONTEXT_FAILED":
            pattern_logs = [{'patterns': ['Failed to create TSS context.'],
                             'log_explanation': 'TSS（TPM Software Stack，TPM芯片软件栈）上下文初始化失败',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_EPOLL_FAILED":
            pattern_logs = [{'patterns': ['Failed to create epoll service.'],
                             'log_explanation': 'PTS模块创建epoll（I/O event notification facility）服务失败',
                             'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_HASH_FAILED":
            pattern_logs = [{'patterns': ['Failed to create hash table.'], 'log_explanation': 'PTS模块创建HASH表失败',
                             'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_SELFVERIFY_COUNTER_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to create selfverify counter.'], 'log_explanation': '可信自检的IML计数器创建失败，此时可信自检功能不可用',
                 'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_SELFVERIFY_TIMER_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to create selfverify timer.'], 'log_explanation': '周期可信自检的定时器创建失败，此时周期可信自检功能不可用',
                 'log_recommended_action': '·          请联系技术支持\n·          可以通过integrity selfverify命令手动执行可信自检'}]

        elif log_type_desc == "PTS_CREATE_SOCKET_FAILED":
            pattern_logs = [{'patterns': ['Failed to create socket service.'], 'log_explanation': 'PTS模块创建socket服务失败',
                             'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_CREATE_TIMER_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to create timer.'], 'log_explanation': '创建定时器失败\n当PTS模块的任一定时器创建失败时，都会产生本日志',
                 'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_LOAD_KEY_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to load attestation key %{DATA:akName}.'], 'log_explanation': '向TPM芯片加载AK密钥失败',
                 'log_recommended_action': '1.      检查指定名称的AK密钥是否存在且处于使能状态（相关显示命令为display tcsm key name）\n2.      请联系技术支持'}]

        elif log_type_desc == "PTS_PARSE_IML_FAILED":
            pattern_logs = [{'patterns': ['Failed to parse IML.'], 'log_explanation': '可信度量日志解析失败',
                             'log_recommended_action': '1.      依次执行undo pts和pts命令重启PTS服务\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_PKG_PCR_FAILED":
            pattern_logs = [{'patterns': [
                'Hash value computed based on Package IML is not consistent with that in PCR \\(%{NUMBER:pcrIndex:int}\\).'],
                             'log_explanation': '使用Comware软件包的可信度量日志计算出来的HASH值与保存在PCR中的HASH值不同，此时Comware软件包不可信',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_READ_PCR_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to read PCR \\(%{NUMBER:pcrIndex:int}\\).'], 'log_explanation': 'PCR数据读取失败',
                 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_RM_FILE_FAILED":
            pattern_logs = [
                {'patterns': ['Wrong signature for RM file %{DATA:rmFileName}.'], 'log_explanation': 'RM文件签名错误',
                 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_RUNTIME_PCR_FAILED":
            pattern_logs = [{'patterns': [
                'Hash value computed based on runtime IML is not consistent with that in PCR \\(%{NUMBER:pcrIndex:int}\\).'],
                             'log_explanation': '使用Runtime（运行的软件进程）相关的可信度量日志计算出来的HASH值与保存在PCR中的HASH值不同，此时Runtime相关的可执行文件不可信',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "PTS_SELFVERIFY_FAILED":
            pattern_logs = [
                {'patterns': ["Failed to start integrity selfverify. Reason: TPM doesn't exist or isn't enabled."],
                 'log_explanation': '由于TPM芯片不存在或者被禁用，可信自检启动失败',
                 'log_recommended_action': '查看设备的可信计算芯片信息（相关显示命令为display tcsm trusted-computing-chip），确保TPM芯片可用'}]

        elif log_type_desc == "PTS_SELFVERIFY_START_FAILED":
            pattern_logs = [{'patterns': ['Failed to start selfverify.'], 'log_explanation': '启动可信自检失败',
                             'log_recommended_action': '1.      尝试重新启动可信自检\n2.      如果问题仍然存在，请联系技术支持'}]

        elif log_type_desc == "PTS_TEMPLATE_HASH_FAILED":
            pattern_logs = [{'patterns': [
                'Calculated template hash value of %{DATA:nameFileWantMeasureIntegrity} is not consistent with that in IML.'],
                             'log_explanation': '根据目标文件的HASH值和日志度量时间等参数计算的模板HASH值与可信度量日志中的模板HASH值不同，此时该可信度量日志内容可能被篡改',
                             'log_recommended_action': '请联系技术支持'}]


    elif module == "INQA":

        if log_type_desc == "INQA_BWD_LOSS_EXCEED":
            pattern_logs = [{'patterns': [
                'Packet loss rate of the backward flow in instance %{NUMBER:param0:int} exceeded the upper limit.'],
                             'log_explanation': '反向流的丢包率大于丢包超限告警值', 'log_recommended_action': '检查当前组网环境，查看物理线路是否正常'}]

        elif log_type_desc == "INQA_BWD_LOSS_RECOV":
            pattern_logs = [
                {'patterns': ['Packet loss rate of the backward flow in instance %{NUMBER:param0:int} recovered.'],
                 'log_explanation': '反向流的丢包率恢复到正常状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "INQA_DEBUG_FAIL":
            pattern_logs = [
                {'patterns': ['Setting debugging switch to drive failed.'], 'log_explanation': 'iNQA Debug开关配置下发驱动失败',
                 'log_recommended_action': '删除iNQA Debug开关配置，重新配置'}]

        elif log_type_desc == "INQA_FLAG_DIFF":
            pattern_logs = [{'patterns': [
                'Flags of collectors bound with the analyzer instance %{NUMBER:param0:int} are inconsistent.'],
                             'log_explanation': 'Analyzer实例下关联的Collector端配置的染色位不一致',
                             'log_recommended_action': '检查该Analyzer实例下关联的所有Collector端染色位信息，保证配置一致'}]

        elif log_type_desc == "INQA_FLAG_FAIL":
            pattern_logs = [{'patterns': ['Setting coloring bit to drive failed.'], 'log_explanation': '染色位配置下发驱动失败',
                             'log_recommended_action': '使用display qos-acl resource命令查看设备的ACL资源是否足够。如果ACL资源不足，请删除暂时无需使用的ACL后，再重新配置染色位'}]

        elif log_type_desc == "INQA_FLOW_DIFF":
            pattern_logs = [{'patterns': [
                'Flows of collectors bound with the analyzer instance  %{NUMBER:param0:int} are inconsistent.'],
                             'log_explanation': 'Analyzer实例下关联的Collector端发送过来的报文中携带的目标流不一致',
                             'log_recommended_action': '检查该Analyzer实例下关联的所有Collector端配置的目标流，保证目标流的配置一致'}]

        elif log_type_desc == "INQA_FWD_LOSS_EXCEED":
            pattern_logs = [{'patterns': [
                'Packet loss rate of the forward flow in instance %{NUMBER:param0:int} exceeded the upper limit.'],
                             'log_explanation': '正向流的丢包率大于丢包超限告警阈值', 'log_recommended_action': '检查当前组网环境，查看物理线路是否正常'}]

        elif log_type_desc == "INQA_FWD_LOSS_RECOV":
            pattern_logs = [
                {'patterns': ['Packet loss rate of the forward flow in instance %{NUMBER:param0:int} recovered.'],
                 'log_explanation': '正向流的丢包率恢复到正常状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "INQA_INST_FAIL":
            pattern_logs = [{'patterns': ['Setting instance %{NUMBER:param0:int} information to drive failed.'],
                             'log_explanation': '实例配置下发给驱动失败',
                             'log_recommended_action': '使用display qos-acl resource命令查看设备的ACL资源是否足够。如果ACL资源不足，请删除暂时无需使用的ACL后，再重新配置实例'}]

        elif log_type_desc == "INQA_INTVL_DIFF":
            pattern_logs = [{'patterns': [
                'Intervals of collectors bound with analyzer instance %{NUMBER:param0:int} are inconsistent.'],
                             'log_explanation': 'Analyzer实例下关联的Collector端发送过来的报文携带的统计周期值不一致',
                             'log_recommended_action': '检查该Analyzer实例下关联的所有Collector端配置的统计周期，保持配置一致'}]

        elif log_type_desc == "INQA_NO_RESOURCE":
            pattern_logs = [
                {'patterns': ['Failed to configure instance %{NUMBER:param0:int} due to insufficient resources.'],
                 'log_explanation': '由于ACL表项资源不足，导致iNQA实例配置失败',
                 'log_recommended_action': '删除当前不需要使用的iNQA实例，或者删除当前不需要使用的ACL，来释放ACL表项资源，再重新配置当前实例'}]

        elif log_type_desc == "INQA_NO_SUPPORT":
            pattern_logs = [{'patterns': ['iNQA is not supported in this slot.'], 'log_explanation': '指定slot不支持iNQA功能',
                             'log_recommended_action': '更换slot，或者将需要测量的流量切换到支持iNQA的slot上'}]

        elif log_type_desc == "INQA_ SMOOTH_BEGIN_FAIL":
            pattern_logs = [{'patterns': ['Setting smoothing beginning to kernal failed.'],
                             'log_explanation': 'iNQA模块通知内核平滑开始，通知失败', 'log_recommended_action': '请联系技术支持人员'}]

        elif log_type_desc == "INQA_ SMOOTH_END_FAIL":
            pattern_logs = [
                {'patterns': ['Setting smoothing ending to kernal failed.'], 'log_explanation': 'iNQA模块通知内核平滑结束，通知失败',
                 'log_recommended_action': '请联系技术支持人员'}]


    elif module == "IP6ADDR":

        if log_type_desc == "IP6ADDR_CREATEADDRESS_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to create an address by the prefix. Reason: %{DATA:ipv6Prefix} on %{DATA:interfaceName} and %{DATA:ipv6Prefix} on %{DATA:interfaceName} overlap.'],
                             'log_explanation': '当配置接口通过引用前缀生成IPv6地址时，可能由于同一台设备的不同接口前缀覆盖，导致IPv6地址生成失败，此时输出本日志',
                             'log_recommended_action': '取消冲突接口上的通过前缀生成IPv6地址的配置，重新配置其他前缀的IPv6地址'}]

        elif log_type_desc == "IP6ADDR_FUNCTION_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to enable IPv6 on interface %{DATA:interfaceName}. Reason: %{DATA:failureReasons}.'],
                             'log_explanation': '接口通过有状态或无状态方式获取IPv6地址时，或手工指定接口的IPv6地址时，会使能IPv6功能。如果为接口配置IPv6地址失败，即使能IPv6功能失败，则打印此日志。使能IPv6功能失败的原因一般有：资源不足、设备不支持IPv6、未知错误等',
                             'log_recommended_action': '·          如果是因为资源不足，可清理设备内存以释放资源，然后重新执行操作\n·          如果是未知错误，请联系技术支持'}]


    elif module == "IP6FW":

        if log_type_desc == "IPv6_MTU_SET_DRV_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'The operation is not supported to set driver IPv6 interface MTU: interface is %{DATA:interfaceName}, MTU is %{NUMBER:mtuValue:int}.'],
                             'log_explanation': '配置接口GigabitEthernet1/0/1上发送IPv6报文的MTU值，配置不支持下驱动',
                             'log_recommended_action': '1.      对于硬件转发的设备，无需处理，设备不支持配置接口上发送IPv6报文的MTU\n2.      对于软件转发的设备，请联系技术支持'}]


    elif module == "IPADDR":

        if log_type_desc == "IPADDR_HA_EVENT_ERROR":
            pattern_logs = [{'patterns': ['A process failed HA upgrade because %{DATA:haUpgradeFailureReason}.'],
                             'log_explanation': '进程HA升级失败，原因是板间平滑失败，重新升级为主失败等', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "IPADDR_HA_STOP_EVENT":
            pattern_logs = [{'patterns': ['The device received an HA stop event.'], 'log_explanation': '设备收到HA STOP事件',
                             'log_recommended_action': '请联系技术支持'}]


    elif module == "IPFW":

        if log_type_desc == "IPFW_FAILURE":
            pattern_logs = [{'patterns': ["The card doesn't support the split horizon forwarding configuration."],
                             'log_explanation': '单板不支持配置转发水平分割',
                             'log_recommended_action': '1.      请确保所属单板支持转发水平分割配置\n2.      请联系技术支持'},
                            {'patterns': ['Failed to configure split horizon forwarding on the card.'],
                             'log_explanation': '单板配置转发水平分割失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "IPv4_MTU_SET_DRV_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'The operation is not supported to set driver IPv4 interface MTU: interface is %{DATA:interfaceName}, MTU is %{NUMBER:mtuValue:int}.'],
                             'log_explanation': '配置接口GigabitEthernet1/0/1上发送IPv4报文的MTU值，配置不支持下驱动',
                             'log_recommended_action': '1.      对于硬件转发的设备，无需处理，设备不支持配置接口上发送IPv4报文的MTU\n2.      对于软件转发的设备，请联系技术支持'}]


    elif module == "NAT":

        if log_type_desc == "NAT_FAILED_ADD_FLOW_TABLE":
            pattern_logs = [{'patterns': ['Failed to add flow-table due to %{DATA:failureReason}.'],
                             'log_explanation': '添加流表失败，可能原因包括硬件资源不足、NAT配置地址存在重叠等',
                             'log_recommended_action': '对于硬件资源不足情况，请联系技术支持\n对于NAT配置地址存在重叠情况，请尽量避免出现部分地址重叠，如果不可避免，请将重叠部分地址和不重叠地址分开，单独配置'}]

        elif log_type_desc == "NAT_ADDR_BIND_CONFLICT":
            pattern_logs = [{'patterns': [
                'Failed to activate NAT configuration on interface %{DATA:interfaceName}, because global IP addresses already bound to another service card.'],
                             'log_explanation': '配置中的外网地址绑定指定业务板时发现其已经绑定到其他业务板上，则触发该日志',
                             'log_recommended_action': '如果有多个接口引用了相同的外网地址，则这些接口必须指定同一块业务板进行NAT处理。请使用display nat all命令检查配置，并修改配置使引用相同外网地址的接口绑定相同的业务板。另外，由于该绑定冲突，失效配置需要先删除，再重新进行配置'}]

        elif log_type_desc == "NAT_FAILED_ADD_FLOW_RULE":
            pattern_logs = [{'patterns': ['Failed to add flow-table due to: %{DATA:reasonFailure}.'],
                             'log_explanation': '添加流表失败，可能原因包括硬件资源不足、内存不足等', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "NAT_SERVER_INVALID":
            pattern_logs = [{'patterns': [
                'The NAT server with Easy IP is invalid because its global settings conflict with that of another NAT server on this interface.'],
                             'log_explanation': 'Easy IP方式的NAT服务器配置生效时发现同一个接口下存在其他NAT服务器配置也包含相同的外网信息，则触发该日志',
                             'log_recommended_action': '同一个接口下配置的NAT服务器，其协议类型、外网地址和外网端口号的组合必须是唯一的。请修改相应接口的NAT服务器配置'}]

        elif log_type_desc == "NAT_SERVICE_CARD_RECOVER_FAILURE":
            pattern_logs = [{'patterns': [
                'Failed to recover the configuration of binding the service card on slot %{NUMBER:slotNumber:int} to interface %{DATA:interfaceName}, because %{DATA:reasonsRestoringBindingServiceCardInterfaceFails}.',
                'Failed to recover the configuration of binding the service card on chassis %{NUMBER:chassisNumber:int} slot %{NUMBER:slotNumber:int} to interface %{DATA:interfaceName}, because %{DATA:reasonsRestoringBindingServiceCardInterfaceFails}.'],
                             'log_explanation': '恢复接口绑定业务板配置失败时触发该日志',
                             'log_recommended_action': '·          如果提示NAT地址已经绑定到其他业务板，则使用display nat all检查配置，并修改配置使引用相同外网地址的接口绑定相同的业务板\n·          如果提示业务板不支持NAT业务、硬件资源不足或者未知错误，请排查业务板的硬件问题'}]


    elif module == "IPSEC":

        if log_type_desc == "IPSEC_PACKET_DISCARDED":
            pattern_logs = [{'patterns': [
                'IPsec packet discarded, Src IP:%{DATA:sourceIpAddress}, Dst IP:%{DATA:destinationIpAddress}, SPI:%{NUMBER:securityParameterIndex\\(spi\\):int}, SN:%{NUMBER:sequenceNumberPacket:int}, Cause:%{DATA:reasonDroppingPacket}.'],
                             'log_explanation': 'IPsec报文被丢弃', 'log_recommended_action': '无'}]

        elif log_type_desc == "IPSEC_SA_ESTABLISH":
            pattern_logs = [{'patterns': [
                'Established IPsec SA. The SA’s source address is %{DATA:param0}, destination address is %{DATA:param1}, protocol is %{DATA:param2}, and SPI is %{NUMBER:param3:int}.'],
                             'log_explanation': 'IPsec SA创建成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "IPSEC_SA_ESTABLISH_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to establish IPsec SA for the reason of %{DATA:reasonIpsecSaEstablishmentFailure}. The SA’s source address is %{DATA:sourceAddress}, and its destination address is %{DATA:destinationAddress}.'],
                             'log_explanation': 'IPsec SA创建失败。触发该日志的原因可能有：隧道创建失败、配置不完整、或者配置的安全提议无效',
                             'log_recommended_action': '检查本端和对端设备上的IPsec配置'}]

        elif log_type_desc == "IPSEC_SA_INITINATION":
            pattern_logs = [{'patterns': [
                'Began to establish IPsec SA. The SA’s source address is %{DATA:param0}, and its destination address is %{DATA:param1}.'],
                             'log_explanation': '开始创建IPsec SA', 'log_recommended_action': '无'}]

        elif log_type_desc == "IPSEC_SA_TERMINATE":
            pattern_logs = [{'patterns': [
                'The IPsec SA was deleted for the reason of %{DATA:reasonIpsecSaRemoval}. The SA’s source address is %{DATA:sourceAddress}, destination address is %{DATA:destinationAddress}, protocol is %{DATA:securityProtocol}, and SPI is %{NUMBER:spi:int}.'],
                             'log_explanation': 'IPsec SA被删除。触发该日志的原因可能有：SA空闲超时或者执行了reset命令',
                             'log_recommended_action': '无'}]


    elif module == "IPSG":

        if log_type_desc == "IPSG_ADDENTRY_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to add an IP source guard binding \\(IP %{DATA:ipv4AddressIpv6Address}, MAC %{DATA:macAddress}, and VLAN %{NUMBER:vlanId:int}\\) on interface %{DATA:interfaceName}. %{DATA:failureReasons}.'],
                             'log_explanation': '下发静态或动态IP Source Guard绑定表项失败，可能的原因有：特性不支持、资源不足、表项达到最大规格或未知错误',
                             'log_recommended_action': '·          当提示硬件资源不足时，可清理设备内存以释放资源\n·          当下发是静态IP Source Guard绑定表项时，可重新执行命令下发该表项\n·          当下发静态或动态IP Source Guard绑定表项失败原因为未知错误时，请联系技术支持'}]

        elif log_type_desc == "IPSG_ADDEXCLUDEDVLAN_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to add excluded VLANs \\(start VLAN %{NUMBER:startVlanIdVlanRangeConfiguredExcludedIpsgFiltering:int} to end VLAN %{NUMBER:endVlanIdVlanRangeConfiguredExcludedIpsgFiltering:int}\\). %{DATA:failureReasons}.'],
                             'log_explanation': '下发免过滤VLAN失败，可能的原因有：特性不支持、资源不足或未知错误',
                             'log_recommended_action': '·          因硬件资源不足而引起的免过滤VLAN下发失败，可清理设备内存以释放资源，然后重新执行命令下发该配置\n·          当下发免过滤VLAN失败原因为未知错误时，请联系技术支持'}]

        elif log_type_desc == "IPSG_ARP_LOCALMAC_CONFLICT":
            pattern_logs = [{'patterns': [
                'MAC conflict exists between an ARP entry and a local entry: IP=%{DATA:ipAddress}, VPN=%{DATA:vpnInstanceName}, ARPMAC=%{DATA:macAddressArpEntry}, LocalMAC=%{DATA:macAddressLocalIpsgBinding}.'],
                             'log_explanation': 'ARP表项和本地绑定表项的MAC地址冲突。当存在恶意的ARP攻击时，如果ARP表项和本地绑定表项的IP地址相同，但两者的MAC地址不同，则会输出该日志',
                             'log_recommended_action': '检查ARP表项的来源设备是否存在恶意攻击行为'}]

        elif log_type_desc == "IPSG_ARP_REMOTEMAC_CONFLICT":
            pattern_logs = [{'patterns': [
                'MAC conflict exists between an ARP entry and a remote entry: IP=%{DATA:ipAddress}, VPN=%{DATA:vpnInstanceName}, ARPMAC=%{DATA:macAddressArpEntry}, RemoteMAC=%{DATA:macAddressRemoteIpsgBinding}.'],
                             'log_explanation': 'ARP表项和远端绑定表项的MAC地址冲突，有以下情况会输出该日志：\n·          存在恶意的ARP攻击，设备学习到非法用户的ARP表项与远端绑定表项的IP地址相同，但两者的MAC地址不同\n·          远端用户漫游到本地上线，使得设备学习到该漫游用户的ARP表项与远端绑定表项的IP地址相同，但两者的MAC地址不同',
                             'log_recommended_action': '·          当存在恶意ARP攻击时，请检查ARP表项的来源设备\n·          对于漫游用户本地上线，无需处理'}]

        elif log_type_desc == "IPSG_DELENTRY_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to delete an IP source guard binding \\(IP %{DATA:ipAddress}, MAC %{DATA:macAddress}, and VLAN %{NUMBER:vlanId:int}\\) on interface %{DATA:interfaceName}. %{DATA:failureReason}.'],
                             'log_explanation': '删除全局静态IP Source Guard绑定表项失败，可能的原因有：特性不支持或者未知错误',
                             'log_recommended_action': '·          重新执行命令删除该表项\n·          当删除全局静态IP Source Guard绑定表项失败原因为未知错误时，请联系技术支持'}]

        elif log_type_desc == "IPSG_DELEXCLUDEDVLAN_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to delete excluded VLANs \\(start VLAN %{NUMBER:startVlanIdVlanRangeConfiguredExcludedIpsgFiltering:int} to end VLAN %{NUMBER:endVlanIdVlanRangeConfiguredExcludedIpsgFiltering:int}\\). %{DATA:failureReasons}.'],
                             'log_explanation': '删除免过滤VLAN失败，可能的原因有：特性不支持、资源不足或未知错误',
                             'log_recommended_action': '·          因硬件资源不足而引起的删除免过滤VLAN失败，可清理设备内存以释放资源，然后重新执行命令下发该配置\n·          当删除免过滤VLAN失败原因为未知错误时，请联系技术支持'}]

        elif log_type_desc == "IPSG_MAC_CONFLICT":
            pattern_logs = [{'patterns': [
                'MAC conflict exists between a local entry and a remote entry: IP=%{DATA:ipAddress}, VPN=%{DATA:vpnInstanceName}, LocalMAC=%{DATA:macAddressLocalIpsgBinding}, RemoteMAC=%{DATA:macAddressRemoteIpsgBinding}.'],
                             'log_explanation': '远端绑定表项和本地绑定表项的MAC地址冲突。当本地学习到一个远端绑定表项时，若该绑定表项的IP地址与本地已有某绑定表项的IP地址相同，但两者的MAC地址不同，则会输出该日志',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "IPSG_ND_LOCALMAC_CONFLICT":
            pattern_logs = [{'patterns': [
                'MAC conflict exists between an ND entry and a local entry: IPv6=%{DATA:ipAddress}, VPN=%{DATA:vpnInstanceName}, NDMAC=%{DATA:macAddressNdEntry}, LocalMAC=%{DATA:macAddressLocalIpsgBinding}.'],
                             'log_explanation': 'ND表项和本地绑定表项的MAC地址冲突。当存在恶意的ND攻击时，如果ND表项和本地绑定表项的IP地址相同，但两者的MAC地址不同，则会输出该日志',
                             'log_recommended_action': '检查ND表项的来源设备是否存在恶意攻击行为'}]

        elif log_type_desc == "IPSG_ND_REMOTEMAC_CONFLICT":
            pattern_logs = [{'patterns': [
                'MAC conflict exists between an ND entry and a remote entry: IPv6=%{DATA:ipAddress}, VPN=%{DATA:vpnInstanceName}, NDMAC=%{DATA:macAddressNdEntry}, RemoteMAC=%{DATA:macAddressRemoteIpsgBinding}.'],
                             'log_explanation': 'ND表项和远端绑定表项的MAC地址冲突，有以下情况会输出该日志：\n·          存在恶意的ND攻击，设备学习到非法用户的ND表项与远端绑定表项的IPv6地址相同，但两者的MAC地址不同\n·          远端用户漫游到本地上线，使得设备学习到该漫游用户的ND表项与远端绑定表项的IPv6地址相同，但两者的MAC地址不同',
                             'log_recommended_action': '·          当存在恶意ARP攻击时，请检查ND表项的来源设备\n·          对于漫游用户本地上线，无需处理'}]

        elif log_type_desc == "IPSG_IPV6_ALARMCLEAR":
            pattern_logs = [{'patterns': [
                'The packet dropping rate on %{DATA:interfaceName} dropped below %{NUMBER:ipv6sgAlarmThreshold:int} pps.'],
                             'log_explanation': '接口上每秒丢弃报文数恢复到告警阈值之内', 'log_recommended_action': '无'}]

        elif log_type_desc == "IPSG_IPV6_ALARMEMERGE":
            pattern_logs = [{'patterns': [
                'The packet dropping rate on %{DATA:interfaceName} reached or exceeded %{NUMBER:ipv6sgAlarmThreshold:int} pps.'],
                             'log_explanation': '接口上每秒丢弃报文数大于或等于告警阈值', 'log_recommended_action': '检查遭到攻击的接口下是否存在攻击源'}]


    elif module == "IRDP":

        if log_type_desc == "IRDP_EXCEED_ADVADDR_LIMIT":
            pattern_logs = [{'patterns': [
                'The number of advertisement addresses on interface %{DATA:interfaceName} exceeded the limit 255.'],
                             'log_explanation': '接口上待通告的地址数超过了上限值', 'log_recommended_action': '删除接口上不需要的地址'}]


    elif module == "IRF":

        if log_type_desc == "IRF_LINK_BLOCK":
            pattern_logs = [{'patterns': ['IRF port went blocked.'],
                             'log_explanation': 'IRF端口链路状态变为blocked。处于该状态的IRF端口不能转发数据报文，只能收发IRF协议报文。例如，检测到成员编号冲突时，优先级低的设备上会打印该日志信息',
                             'log_recommended_action': '请确认组网中是否存在成员编号冲突的设备。如果存在，请将成员编号修改为不同的值'}]

        elif log_type_desc == "IRF_LINK_DOWN":
            pattern_logs = [{'patterns': ['IRF port went down.'], 'log_explanation': 'IRF端口链路状态变为down',
                             'log_recommended_action': '请确认：\n·          IRF端口下是否绑定了物理接口\n·          绑定的物理接口是否和对端正确连接'}]

        elif log_type_desc == "IRF_LINK_UP":
            pattern_logs = [
                {'patterns': ['IRF port came up.'], 'log_explanation': 'IRF端口链路状态变为up', 'log_recommended_action': '无'}]

        elif log_type_desc == "IRF_MEMBERID_CONFLICT":
            pattern_logs = [{'patterns': [
                'IRF member ID conflict occurred. The ID %{NUMBER:irfMemberIdDevice:int} has been used for another device with CPU-Mac: %{DATA:cpuMacAddressDevice}.'],
                             'log_explanation': '在同一广播域中发现跟自己成员编号相同的设备时，打印该日志，提示成员冲突',
                             'log_recommended_action': '根据提示信息，检查IRF中的成员编号，重新设置新加入设备的成员编号'}]


    elif module == "STM":

        if log_type_desc == "STM_MERGE":
            pattern_logs = [
                {'patterns': ['IRF merge occurred.'], 'log_explanation': 'IRF合并事件发生', 'log_recommended_action': '无'}]

        elif log_type_desc == "STM_MERGE_NEED_REBOOT":
            pattern_logs = [{'patterns': ['IRF merge occurred. This IRF system needs a reboot.'],
                             'log_explanation': '由于本IRF系统在主设备选举中失败，请重启本IRF系统来完成IRF合并',
                             'log_recommended_action': '登录到本IRF，使用reboot命令重启本IRF'}]

        elif log_type_desc == "STM_MERGE_NOT_NEED_REBOOT":
            pattern_logs = [{'patterns': ['IRF merge occurred. This IRF system does not need to reboot.'],
                             'log_explanation': '由于本IRF系统在主设备选举中取胜，无须重启本IRF系统即可完成IRF合并',
                             'log_recommended_action': '重启对端IRF完成合并'}]

        elif log_type_desc == "STM_AUTO_UPDATE_FAILED":
            pattern_logs = [{'patterns': [
                'Slot %{NUMBER:irfMemberId:int} auto-update failed. Reason: %{DATA:failureReason}.',
                'Chassis %{NUMBER:irfMemberId:int} slot %{NUMBER:slotNumberMpu:int} auto-update failed. Reason: %{DATA:failureReason}.'],
                             'log_explanation': '形式一：\n在加入IRF时，从设备从主设备自动加载启动软件包失败\n形式二：\n在加入IRF时，备用主控板从全局主用主控板自动加载启动软件包失败',
                             'log_recommended_action': '1.      如果失败原因为Timeout when loading，请检查IRF链路是否畅通\n2.      如果失败原因为Wrong description when loading，可能是软件包被损坏了，请重新下载软件包\n3.      如果失败原因为Disk full when writing to disk，请先清理备设备的存储介质，删除一些暂时不用的文件\n4.      请手动升级即将加入IRF的设备的软件包后，再将该设备和IRF相连'}]

        elif log_type_desc == "STM_AUTO_UPDATED_FINISHED":
            pattern_logs = [{'patterns': ['File loading finished on slot %{NUMBER:param0:int}.',
                                          'File loading finished on chassis %{NUMBER:param1:int} slot %{NUMBER:param2:int}.'],
                             'log_explanation': '形式一：\n成员设备完成启动文件加载\n形式二：\n主控板完成启动文件加载', 'log_recommended_action': '无'}]

        elif log_type_desc == "STM_AUTO_UPDATING":
            pattern_logs = [{'patterns': ["Don't reboot the slot %{NUMBER:irfMemberId:int}. It is loading files.",
                                          "Don't reboot the chassis %{NUMBER:irfMemberId:int} slot %{NUMBER:slotNumberMpu:int}. It is loading files."],
                             'log_explanation': '形式一：\n如果成员设备正在加载文件，请不要重启该设备\n形式二：\n如果主控板正在加载文件，请不要重启该主控板',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "STM_HELLOPKT_NOTSEND":
            pattern_logs = [{'patterns': ["Hello thread hasn't sent packets for %{NUMBER:timeValue:int} seconds."],
                             'log_explanation': 'Hello线程发包时间间隔超过10秒，记录发包超时时间',
                             'log_recommended_action': '执行display cpu-usage查看系统是不是暂时的CPU利用率增高，例如受到攻击或者处理其他较耗费CPU资源的任务。如果不能定位原因请联系技术支持。需要注意的是，如果Hello报文发包时间超过心跳超时时间会造成IRF分裂'}]

        elif log_type_desc == "STM_HELLOPKT_NOTRCV":
            pattern_logs = [{'patterns': ["Hello thread hasn't received packets for %{NUMBER:timeValue:int} seconds."],
                             'log_explanation': 'Hello线程收包时间超过10秒，记录收包超时的时间',
                             'log_recommended_action': '执行display cpu-usage查看系统是不是暂时的CPU利用率增高，例如受到攻击或者处理其他较耗费CPU资源的任务。如果不能定位原因请联系技术支持。需要注意的是，如果长时间收不到Hello报文会导致IRF分裂'}]

        elif log_type_desc == "STM_LINK_DOWN":
            pattern_logs = [{'patterns': ['IRF port %{NUMBER:irfPortName:int} went down.'],
                             'log_explanation': 'IRF端口关闭。当绑定的所有物理端口都关闭时，IRF端口关闭',
                             'log_recommended_action': '检查绑定到IRF端口的物理端口，确保至少有一个物理端口处于UP状态，可以正常工作'}]

        elif log_type_desc == "STM_LINK_TIMEOUT":
            pattern_logs = [
                {'patterns': ['IRF port %{NUMBER:irfPortName:int} went down because the heartbeat timed out.'],
                 'log_explanation': '由于心跳检测超时，IRF端口关闭', 'log_recommended_action': '检查IRF链路是否故障'}]

        elif log_type_desc == "STM_LINK_UP":
            pattern_logs = [
                {'patterns': ['IRF port %{NUMBER:irfPortName:int} came up.'], 'log_explanation': 'IRF链路可以正常工作',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "STM_PHY_DOWN":
            pattern_logs = [
                {'patterns': ['Physical interface %{DATA:param0} of IRF port %{NUMBER:param1:int} went down.'],
                 'log_explanation': 'IRF物理端口状态变为down', 'log_recommended_action': '请检查IRF物理端口线缆连接情况'}]

        elif log_type_desc == "STM_PHY_UP":
            pattern_logs = [
                {'patterns': ['Physical interface %{DATA:param0} of IRF port %{NUMBER:param1:int} came up.'],
                 'log_explanation': 'IRF物理端口状态变为UP', 'log_recommended_action': '无'}]

        elif log_type_desc == "STM_SAMEMAC":
            pattern_logs = [{'patterns': ['Failed to stack because of the same bridge MAC addresses.'],
                             'log_explanation': '因为桥MAC地址相同，无法形成IRF', 'log_recommended_action': '检查设备桥MAC地址是否相同'}]

        elif log_type_desc == "STM_SOMER_CHECK":
            pattern_logs = [{'patterns': ['Neighbor of IRF port %{NUMBER:irfPortName:int} cannot be stacked.'],
                             'log_explanation': 'IRF口连接的设备无法加入本设备所在的IRF',
                             'log_recommended_action': '请检查以下事项：\n·          设备型号是否允许组成IRF\n·          IRF配置是否正确\n要获取更多信息，请参见该型号设备的IRF配置指导'}]


    elif module == "ISIS":

        if log_type_desc == "ISIS_LSP_CONFLICT":
            pattern_logs = [{'patterns': [
                'IS-IS %{NUMBER:is-isProcessId:int}, %{DATA:isType} LSP, LSPID=%{DATA:lspId}, SeqNum=%{DATA:lspSequenceNumber}, system ID conflict might exist.'],
                             'log_explanation': '网络中可能存在System ID冲突',
                             'log_recommended_action': '检查产生该LSP的设备的System ID是否和其他设备的System ID冲突'}]

        elif log_type_desc == "ISIS_MEM_ALERT":
            pattern_logs = [{'patterns': ['ISIS Process received system memory alert %{DATA:typeMemoryAlarm} event.'],
                             'log_explanation': 'IS-IS模块收到内存告警信息',
                             'log_recommended_action': '当超过各级内存门限时，检查系统内存占用情况，对占用内存较多的模块进行调整，尽量释放可用内存'}]

        elif log_type_desc == "ISIS_NBR_CHG":
            pattern_logs = [{'patterns': [
                'IS-IS %{NUMBER:is-isProcessId:int}, %{DATA:neighborLevel} adjacency %{DATA:neighborId} \\(%{DATA:interfaceName}\\), state changed to %{DATA:currentNeighborState}, Reason: %{DATA:reasonNeighborStateChange}.'],
                             'log_explanation': '邻居状态发生变化',
                             'log_recommended_action': '需要关注邻居状态变化原因。当邻居状态变为down时，检查IS-IS配置正确性和网络连通性'}]


    elif module == "ISSU":

        if log_type_desc == "ISSU_LOAD_FAILED":
            pattern_logs = [{'patterns': ['Failed to execute the issu load command.'],
                             'log_explanation': '用户执行issu load命令进行ISSU升级，操作失败',
                             'log_recommended_action': '请根据提示信息采取相应措施'}]

        elif log_type_desc == "ISSU_LOAD_SUCCESS":
            pattern_logs = [{'patterns': ['Executed the issu load command successfully.'],
                             'log_explanation': '用户执行issu load命令进行ISSU升级，操作成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "ISSU_PROCESSWITCHOVER":
            pattern_logs = [{'patterns': ['Switchover completed. The standby process became the active process.'],
                             'log_explanation': '用户执行issu run switchover进行主备倒换完成，备进程已升级为主进程',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "ISSU_ROLLBACKCHECKNORMAL":
            pattern_logs = [{'patterns': [
                'The rollback might not be able to restore the previous version for %{DATA:chassisNumberSlotNumberSlotNumber} because the status is not normal.'],
                             'log_explanation': 'ISSU升级，ISSU状态处理Switching，用户执行issu rollback回滚或ISSU回滚定时器超时自动回滚，如果有升级过的板状态不为Normal，会输出该日志',
                             'log_recommended_action': '无'}]


    elif module == "L2PT":

        if log_type_desc == "L2PT_ADD_GROUPMEMBER_FAILED":
            pattern_logs = [{'patterns': [
                'Failed to add %{DATA:interfaceName} as a member to the VLAN tunnel group for %{DATA:protocolName}.'],
                             'log_explanation': '接口加入协议的VLAN Tunnel组播组失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "L2PT_CREATE_TUNNELGROUP_FAILED":
            pattern_logs = [{'patterns': ['Failed to create a VLAN tunnel group for %{DATA:protocolName}.'],
                             'log_explanation': '创建协议的VLAN Tunnel组播组失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "L2PT_ENABLE_DROP_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to enable %{DATA:protocolName} packet drop on %{DATA:interfaceName}.'],
                 'log_explanation': '接口上使能L2PT Drop功能失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "L2PT_SET_MULTIMAC_FAILED":
            pattern_logs = [{'patterns': ['Failed to set a tunnel destination MAC address to %{MAC:macAddress}.'],
                             'log_explanation': '配置BPDU Tunnel报文的目的MAC地址失败', 'log_recommended_action': '无'}]


    elif module == "L2TPV2":

        if log_type_desc == "L2TPV2_SESSION_EXCEED_LIMIT":
            pattern_logs = [{'patterns': ['Number of L2TP sessions exceeded the limit.'],
                             'log_explanation': '设备上建立的L2TP会话数目已经达到最大值', 'log_recommended_action': '无'}]

        elif log_type_desc == "L2TPV2_TUNNEL_EXCEED_LIMIT":
            pattern_logs = [
                {'patterns': ['Number of L2TP tunnels exceeded the limit.'], 'log_explanation': '设备上建立的L2TP隧道数目已经达到最大值',
                 'log_recommended_action': '要想建立新的L2TP隧道，可以通过reset l2tp tunnel命令立即断开空闲的L2TP隧道，或等待Hello定时器超时后设备自动断开空闲的L2TP隧道'}]


    elif module == "L2VPN":

        if log_type_desc == "L2VPN_ARP_MOBILITY_SUPPRESS":
            pattern_logs = [{'patterns': [
                'ARP \\(IP %{DATA:ipAddress}, MAC %{DATA:macAddress}\\) was suppressed in the public instance due to frequent ARP mobility events.'],
                             'log_explanation': '开启ARP反复迁移抑制功能后，ARP迁移频率超过限制，抑制该ARP迁移',
                             'log_recommended_action': 'ARP迁移频率过高的原因可能是网络中存在IP地址冲突。请检查网络中的IP地址配置，避免IP地址冲突'}, {
                                'patterns': [
                                    'ARP \\(IP %{DATA:ipAddress}, MAC %{DATA:macAddress}\\) was suppressed in VPN instance %{DATA:vpnInstanceName} due to frequent ARP mobility events.'],
                                'log_explanation': '开启ARP反复迁移抑制功能后，ARP迁移频率超过限制，抑制该ARP迁移',
                                'log_recommended_action': 'ARP迁移频率过高的原因可能是网络中存在IP地址冲突。请检查网络中的IP地址配置，避免IP地址冲突'}]

        elif log_type_desc == "L2VPN_ARP_MOBILITY_UNSUPPRESS":
            pattern_logs = [{'patterns': [
                'ARP \\(IP %{DATA:param0}, MAC %{DATA:param1}\\) was unsuppressed in the public instance.'],
                             'log_explanation': '执行undo evpn route arp-mobility suppress命令后，解除指定ARP的迁移抑制，可以向远端通告该ARP信息',
                             'log_recommended_action': '无'}, {'patterns': [
                'ARP \\(IP %{DATA:ipAddress}, MAC %{DATA:macAddress}\\) was unsuppressed in VPN instance %{DATA:vpnInstanceName}.'],
                                                              'log_explanation': '执行undo evpn route arp-mobility suppress命令后，解除指定ARP的迁移抑制，可以向远端通告该ARP信息',
                                                              'log_recommended_action': '无'}]

        elif log_type_desc == "L2VPN_MAC_MOBILITY_SUPPRESS":
            pattern_logs = [{'patterns': [
                'MAC address %{DATA:macAddress} was suppressed in VSI %{DATA:vsiName} due to frequent MAC mobility events.'],
                             'log_explanation': '开启MAC地址反复迁移抑制功能后，MAC地址迁移频率超过限制，抑制该MAC地址迁移',
                             'log_recommended_action': 'MAC地址迁移频率过高的原因可能是网络中存在MAC地址冲突。请检查网络中的MAC地址配置，避免MAC地址冲突'}]

        elif log_type_desc == "L2VPN_MAC_MOBILITY_UNSUPPRESS":
            pattern_logs = [{'patterns': ['MAC address %{DATA:macAddress} was unsuppressed in VSI %{DATA:vsiName}.'],
                             'log_explanation': '执行undo evpn route mac-mobility suppress命令后，解除指定MAC地址的迁移抑制，可以向远端通告该MAC地址',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "L2VPN_BGPVC_CONFLICT_LOCAL":
            pattern_logs = [{'patterns': [
                'Remote site ID %{NUMBER:idRemoteSite:int} \\(From %{DATA:ipAddressRemoteSite}, route distinguisher %{DATA:routeDistinguisherRemoteSite}\\) conflicts with local site.'],
                             'log_explanation': '本端Site ID和另一个远端Site ID冲突。触发该日志的原因可能有：\n·          新接收到一个远端Site ID和本端Site ID相同\n·          新配置本端Site ID和已接收到的一个远端Site ID相同',
                             'log_recommended_action': '更改远端或本端Site ID，或者修改配置使得远端Site不引入到本端Site所在实例'}]

        elif log_type_desc == "L2VPN_BGPVC_CONFLICT_REMOTE":
            pattern_logs = [{'patterns': [
                'Remote site ID %{NUMBER:idRemoteSite:int} \\(From %{DATA:ipAddressRemoteSite}, route distinguisher %{DATA:routeDistinguisherRemoteSite}\\) conflicts with another remote site.'],
                             'log_explanation': '两个远端的Site ID冲突。触发该日志的原因可能为：在已经接收一个远端Site的情况下，接收到另一个远端Site，两者的Site ID相同',
                             'log_recommended_action': '更改其中一个远端Site ID，或者修改配置使得两个远端不引入到同一个实例中'}]

        elif log_type_desc == "L2VPN_HARD_RESOURCE_NOENOUGH":
            pattern_logs = [{'patterns': ['No enough hardware resource for L2VPN.'], 'log_explanation': 'L2VPN硬件资源不足',
                             'log_recommended_action': '请检查是否生成了当前业务不需要的VSI、PW或AC，是则删除对应配置'}]

        elif log_type_desc == "L2VPN_HARD_RESOURCE_RESTORE":
            pattern_logs = [
                {'patterns': ['Hardware resources for L2VPN are restored.'], 'log_explanation': 'L2VPN硬件资源恢复',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "L2VPN_LABEL_DUPLICATE":
            pattern_logs = [{'patterns': [
                'Incoming label %{NUMBER:incomingLabelValue:int} for a static PW in %{DATA:typeL2vpn} %{DATA:nameXconnect-groupVsi} is duplicate.'],
                             'log_explanation': '交叉连接组或者VSI的静态PW的入标签被静态LSP或者静态CRLSP占用。触发该日志的原因可能有：\n·          在MPLS已使能的情况下，配置了一条入标签被静态LSP或者静态CRLSP占用的静态PW\n·          在入标签被静态LSP或静态CRLSP占用的静态PW存在的情况下，使能MPLS',
                             'log_recommended_action': '删除该静态PW，重新配置一条静态PW，并指定新的入标签值'}]

        elif log_type_desc == "L2VPN_MLAG_AC_CONFLICT":
            pattern_logs = [{'patterns': [
                'The dynamic AC created for Ethernet service instance %{NUMBER:ethernetServiceInstanceId:int} on interface %{DATA:interfaceEthernetServiceInstanceCreated} causes a conflict.'],
                             'log_explanation': 'EVPN支持分布式聚合组网中，IPL链路由隧道切换为聚合链路时，根据不同的静态AC生成的动态AC相互冲突',
                             'log_recommended_action': '删除引发冲突的动态AC对应的静态AC，再重新配置静态AC，并为AC指定合理的报文匹配规则'}]


    elif module == "LAGG":

        if log_type_desc == "LAGG_ACTIVE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the active state.'],
                             'log_explanation': '聚合组内某成员端口成为激活端口', 'log_recommended_action': '无'}]

        elif log_type_desc == "LAGG_AUTO_AGGREGATON":
            pattern_logs = [{'patterns': [
                'Failed to assign automatic assignment-enabled interface %{DATA:portName} to an aggregation group. Please check the configuration on the interface.'],
                             'log_explanation': '开启自动聚合功能后，由于以下原因导致接口无法加入聚合组：\n·          该接口的属性类配置和聚合接口不同\n·          该接口上存在不能加入聚合组的配置',
                             'log_recommended_action': '·          修改对应接口上的属性类配置，以保证和聚合接口一致\n·          删除对应接口上与加入聚合组互斥的功能'}]

        elif log_type_desc == "LAGG_INACTIVE_AICFG":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the port and the aggregate interface had different attribute configurations.'],
                             'log_explanation': '由于聚合组内某成员端口的属性类配置与聚合接口属性类配置不同，该成员端口成为去激活端口',
                             'log_recommended_action': '修改该成员端口的属性类配置，使其与聚合接口属性类配置一致'}]

        elif log_type_desc == "LAGG_INACTIVE_BFD":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the BFD session state of the port was down.'],
                             'log_explanation': '聚合成员端口上的BFD会话down时，该成员端口变为去激活状态',
                             'log_recommended_action': '排查链路故障、检查该非选中状态的成员端口的操作key和属性类配置是否与参考端口一致'}]

        elif log_type_desc == "LAGG_INACTIVE_CONFIGURATION":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the link aggregation configuration of the port was incorrect.'],
                             'log_explanation': '由于聚合组内某成员端口配置限制，该成员端口变为去激活状态',
                             'log_recommended_action': '建议用户检查端口配置的兼容性和正确性'}]

        elif log_type_desc == "LAGG_INACTIVE_DUPLEX":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the duplex mode of the port was different from that of the reference port.'],
                             'log_explanation': '由于聚合组内某成员端口的双工模式与参考端口不一致，该成员端口变为去激活状态',
                             'log_recommended_action': '修改该端口双工模式，使其与参考端口一致'}]

        elif log_type_desc == "LAGG_INACTIVE_HARDWAREVALUE":
            pattern_logs = [{'patterns': [
                "Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because of the port's hardware restriction prevented it from being Selected."],
                             'log_explanation': '聚合组内某成员端口因硬件限制与参考端口不一致，该成员端口变为去激活状态',
                             'log_recommended_action': '将端口移出聚合组'}]

        elif log_type_desc == "LAGG_INACTIVE_IFCFG_DEFAULT":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because no LACPDU was received by the reference port.'],
                             'log_explanation': '由于聚合组内参考端口没有收到对端的LACPDU，该成员端口变为去激活状态',
                             'log_recommended_action': '检查对端是否发送LACPDU'}]

        elif log_type_desc == "LAGG_INACTIVE_IFCFG_LOOPPORT":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the reference port received its own LACPDUs.'],
                             'log_explanation': '由于聚合组内参考端口收到自己的LACPDU，该成员端口变为去激活状态',
                             'log_recommended_action': '检查设备是否存在环路'}]

        elif log_type_desc == "LAGG_INACTIVE_IFCFG_NONAGG":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the link of the port was not aggregatable.'],
                             'log_explanation': '由于聚合组内端口所在链路不可聚合，该成员端口变为去激活状态', 'log_recommended_action': '修改端口配置'}]

        elif log_type_desc == "LAGG_INACTIVE_KEY_INVALID":
            pattern_logs = [{'patterns': [
                "Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the port's operational key was invalid."],
                             'log_explanation': '由于聚合组内成员端口操作Key无效，该成员端口变为去激活状态',
                             'log_recommended_action': '重新配置端口，保证配置符合聚合要求'}]

        elif log_type_desc == "LAGG_INACTIVE_LOWER_LIMIT":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the number of Selected ports was below the lower limit.'],
                             'log_explanation': '因聚合组内激活端口数量未达到配置的最小激活端口数，聚合组内某成员端口变为去激活状态',
                             'log_recommended_action': '增加激活端口数量，使其达到最小激活端口数'}]

        elif log_type_desc == "LAGG_INACTIVE_NODEREMOVE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the card that hosts the port was absent.'],
                             'log_explanation': '由于聚合组内端口所在单板被拔出，该成员端口变为去激活状态',
                             'log_recommended_action': '检查接口所在板是否已插入'}]

        elif log_type_desc == "LAGG_INACTIVE_OPERSTATE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the peer port did not have the Synchronization flag.'],
                             'log_explanation': '由于聚合组对端成员端口所在链路未处于同步状态，本端成员端口变为去激活状态',
                             'log_recommended_action': '检查对端发送的LACPDU'}]

        elif log_type_desc == "LAGG_INACTIVE_PARTNER":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the link aggregation configuration of its peer port was incorrect.'],
                             'log_explanation': '动态聚合组内，由于对端端口聚合配置不正确变为去激活状态，本端端口变为去激活状态',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "LAGG_INACTIVE_PARTNER_KEY_WRONG":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the operational key of the peer port was different from that of the reference port.'],
                             'log_explanation': '由于聚合组对端操作Key与参考端口不一致，本端成员端口变为去激活状态',
                             'log_recommended_action': '修改对端计算操作Key的参数与参考端口一致'}]

        elif log_type_desc == "LAGG_INACTIVE_PARTNER_MAC_WRONG":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the system MAC address of the peer port was different from that of the peer port for the reference port.'],
                             'log_explanation': '由于聚合组对端系统MAC地址与参考端口的对端端口不一致，本端成员端口变为去激活状态',
                             'log_recommended_action': '保证两侧聚合系统的系统MAC地址一致'}]

        elif log_type_desc == "LAGG_INACTIVE_PARTNER_NONAGG":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the link of the peer port was not aggregatable.'],
                             'log_explanation': '由于聚合组内对端端口所在链路不可聚合，本端成员端口变为去激活状态',
                             'log_recommended_action': '修改对端端口配置'}]

        elif log_type_desc == "LAGG_INACTIVE_PARTNER_RDIRHANDLE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because link-aggregation traffic redirection was triggered on the peer port.'],
                             'log_explanation': '由于聚合组对端端口触发聚合重定向功能，本端成员端口变为去激活状态',
                             'log_recommended_action': '修改对端端口配置'}]

        elif log_type_desc == "LAGG_INACTIVE_PHYSTATE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the physical or line protocol state of the port was down.'],
                             'log_explanation': '聚合组内某成员端口处于down状态，该成员端口变为去激活状态',
                             'log_recommended_action': '使该端口处于UP状态'}]

        elif log_type_desc == "LAGG_INACTIVE_PORT_DEFAULT":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the port had not received LACPDUs.'],
                             'log_explanation': '由于聚合组内成员端口未收到LACPDU，该成员端口变为去激活状态',
                             'log_recommended_action': '检查对端是否发送LACPDU'}]

        elif log_type_desc == "LAGG_INACTIVE_RDIRHANDLE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because link-aggregation traffic redirection was triggered on the local port.'],
                             'log_explanation': '由于聚合组本端端口触发聚合重定向功能，该成员端口变为去激活状态', 'log_recommended_action': '修改端口配置'}]

        elif log_type_desc == "LAGG_INACTIVE_ REDUNDANCY":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the port was in secondary state in a redundancy group.'],
                             'log_explanation': '由于聚合组内端口处于冗余备份状态，该成员端口变为去激活状态',
                             'log_recommended_action': '冗余组节点中使本端端口处于工作状态'}]

        elif log_type_desc == "LAGG_INACTIVE_RESOURCE_INSUFICIE":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because hardware resources were not enough.'],
                             'log_explanation': '聚合资源不足导致聚合组内成员端口变为去激活端口', 'log_recommended_action': '无'}]

        elif log_type_desc == "LAGG_INACTIVE_SPEED":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the speed configuration of the port was different from that of the reference port.'],
                             'log_explanation': '聚合组内某成员端口速率与参考端口不一致，该端口变为去激活状态',
                             'log_recommended_action': '修改该端口速率，使其与参考端口一致'}]

        elif log_type_desc == "LAGG_INACTIVE_STANDBY":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the port was in Standby state.'],
                             'log_explanation': '由于聚合组内端口处于standby状态，该成员端口变为去激活状态',
                             'log_recommended_action': '等待一段时间再查看成员端口状态，确认是否处于选中状态，如果处于非选中状态，则根据display link-aggregation troubleshooting命令定位非选中原因及处理建议'}]

        elif log_type_desc == "LAGG_INACTIVE_UPPER_LIMIT":
            pattern_logs = [{'patterns': [
                'Member port %{DATA:portName} of aggregation group %{DATA:linkAggregationGroupTypeId} changed to the inactive state, because the number of Selected ports had reached the upper limit.'],
                             'log_explanation': '动态聚合组内激活端口数量已达到上限。后加入的成员端口成为激活端口，致使某成员端口变为去激活状态',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "LAGG_SELECTPORT_INCONSISTENT":
            pattern_logs = [{'patterns': [
                'The maximum number of Selected ports for %{DATA:linkAggregationGroupTypeId} on PEXs is inconsistent with that on the parent fabric. Please reconfigure this setting.'],
                             'log_explanation': 'PEX设备上聚合组中选中端口数超过了父设备上聚合组的最大选中端口数，需要用户重新配置。触发该日志的原因可能有：以太网接口加入或退出聚合组',
                             'log_recommended_action': '用户重新配置父设备上聚合组的最大选中端口数或减少PEX设备上聚合组的选中端口，使得父设备与PEX设备的最大选中端口数保持一致'}]


    elif module == "LDP":

        if log_type_desc == "LDP_MPLSLSRID_CHG":
            pattern_logs = [
                {'patterns': ['Please reset LDP sessions if you want to make the new MPLS LSR ID take effect.'],
                 'log_explanation': '公网LDP和VPN实例LDP的LSR ID选择方式为：\n1.      如果配置了LDP LSR ID，则LDP的LSR ID为此命令配置的值\n2.      否则，LDP的LSR ID为MPLS LSR ID\n当公网LDP或VPN实例LDP的LSR ID没配置时，修改MPLS LSR ID，会触发该日志。日志提示用户手动重启公网LDP或VPN实例LDP会话使得新配置的MPLS LSR ID生效',
                 'log_recommended_action': '当公网LDP或VPN实例LDP的LSR ID没配置时，使用命令display mpls ldp parameter查看已生效的LSR ID，与配置的MPLS LSR ID 比较，如果不一致，请手动重启LDP会话'}]

        elif log_type_desc == "LDP_SESSION_SP":
            pattern_logs = [{'patterns': [
                "Session \\(%{DATA:peer'sLdpId}, %{DATA:vpnInstance'sName}\\): \\(%{DATA:stateSessionProtection}\\)."],
                             'log_explanation': '当会话的最后一个Link hello邻接关系丢失时，触发该日志。日志显示会话保护过程的状态变化',
                             'log_recommended_action': '检查接口状态和链路状态'}]


    elif module == "PCE":

        if log_type_desc == "PCE_PCEP_SESSION_CHG":
            pattern_logs = [{'patterns': [
                'Session \\(%{DATA:peerAddressSession}, %{DATA:vpnInstanceName}\\) is %{DATA:stateSession}.'],
                             'log_explanation': '显示会话的状态变化以及会话down的原因\ndown 的原因可能包括：\n·          TCP connection down：TCP连接断开\n·          received a close message：收到关闭消息\n·          reception of a malformed PCEP message：收到非法消息\n·          internal error：内部错误\n·          memory in critical state：内存不足\n·          dead timer expired：会话超时\n·          process deactivated：PCE进程去激活\n·          remote peer unavailable/untriggered：对等体失效\n·          reception of an unacceptable number of unrecognized PCEP messages：收到超过限制的未知消息\n·          reception of an unacceptable number of unknown requests/replies：收到超过限制的未知计算请求/计算应答\n·          PCE address changed：PCE地址变化\n·          initialization failed：初始化失败',
                             'log_recommended_action': '如果会话的状态变更为up，不需要进行其它操作\n如果会话的状态变更为down，请根据提示原因检查网络环境或者配置'}]


    elif module == "LLDP":

        if log_type_desc == "LLDP_CREATE_NEIGHBOR":
            pattern_logs = [{'patterns': [
                "%{DATA:param0} agent neighbor created on port %{DATA:param1} \\(IfIndex %{NUMBER:param2:int}\\), neighbor's chassis ID is %{DATA:param3}, port ID is %{DATA:param4}."],
                             'log_explanation': '端口收到新邻居发来的LLDP报文', 'log_recommended_action': '无'}]

        elif log_type_desc == "LLDP_DELETE_NEIGHBOR":
            pattern_logs = [{'patterns': [
                "%{DATA:agentType} agent neighbor deleted on port %{DATA:portName} \\(IfIndex %{NUMBER:portIfindex:int}\\), neighbor's chassis ID is %{DATA:neighbor'sChassisId}, port ID is %{DATA:neighbor'sPortId}."],
                             'log_explanation': '当邻居被删除时，接口收到删除消息', 'log_recommended_action': '无'}]

        elif log_type_desc == "LLDP_LESS_THAN_NEIGHBOR_LIMIT":
            pattern_logs = [{'patterns': [
                'The number of %{DATA:agentType} agent neighbors maintained by port %{DATA:portName} \\(IfIndex %{NUMBER:portIfindex:int}\\) is less than %{NUMBER:maximumNumberNeighborsPortMaintain:int}, and new neighbors can be added.'],
                             'log_explanation': '接口邻居数未达到最大值，还可以为接口增加新邻居', 'log_recommended_action': '无'}]

        elif log_type_desc == "LLDP_NEIGHBOR_AGE_OUT":
            pattern_logs = [{'patterns': [
                "%{DATA:agentType} agent neighbor aged out on port %{DATA:portName} \\(IfIndex %{NUMBER:portIfindex:int}\\), neighbor's chassis ID is %{DATA:neighbor'sChassisId}, port ID is %{DATA:neighbor'sPortId}."],
                             'log_explanation': '当接口在一段时间内没有收到邻居发来的LLDP报文时，打印本信息',
                             'log_recommended_action': '检查链路状态，或者检查对端LLDP的接收和发送状态'}]

        elif log_type_desc == "LLDP_NEIGHBOR_PROTECTION_BLOCK":
            pattern_logs = [{'patterns': [
                'The status of port %{DATA:interfaceName} changed to blocked \\(%{DATA:neighborProtectionFeatureCausedStateChange}\\) for the %{DATA:lldpAgentType} agent.'],
                             'log_explanation': '当接口阻塞时，打印本信息，并且说明阻塞原因',
                             'log_recommended_action': '·          当接口保护类型是aging时：检查链路状态，或者检查两端LLDP的接收和发送状态\n·          当接口保护类型是validation时：检查收到报文的Chassis ID subtype、Chassis ID和Port ID subtype、Port ID值与配置的邻居识别信息是否一致'}]

        elif log_type_desc == "LLDP_NEIGHBOR_PROTECTION_DOWN":
            pattern_logs = [{'patterns': [
                'The status of port %{DATA:interfaceName} changed to down \\(aging\\) for the %{DATA:lldpAgentType} agent.'],
                             'log_explanation': '当端口接收报文超时关闭端口时，打印本信息，并且说明DOWN原因',
                             'log_recommended_action': '当接口保护类型是aging时：检查链路状态，或者检查两端LLDP的接收和发送状态'}]

        elif log_type_desc == "LLDP_NEIGHBOR_PROTECTION_UNBLOCK":
            pattern_logs = [{'patterns': [
                'The status of port %{DATA:interfaceName} changed to unblocked for the %{DATA:lldpAgentType} agent.'],
                             'log_explanation': '当接口由阻塞状态转换为非阻塞状态时，打印本信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "LLDP_NEIGHBOR_PROTECTION_UP":
            pattern_logs = [{'patterns': [
                'The status of port %{DATA:interfaceName} changed to up for the %{DATA:lldpAgentType} agent.'],
                             'log_explanation': '当接口由DOWN状态转换为UP状态时，打印本信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "LLDP_PVID_INCONSISTENT":
            pattern_logs = [{'patterns': [
                'PVID mismatch discovered on %{DATA:portName} \\(PVID %{NUMBER:vlanId:int}\\), with %{DATA:systemName} %{DATA:portName} \\(PVID %{DATA:vlanId}\\).'],
                             'log_explanation': '当邻居的PVID信息与接口本地的PVID不同时，打印本信息',
                             'log_recommended_action': '修改邻居两端的PVID，使其一致'}]

        elif log_type_desc == "LLDP_REACH_NEIGHBOR_LIMIT":
            pattern_logs = [{'patterns': [
                'The number of %{DATA:agentType} agent neighbors maintained by the port %{DATA:portName} \\(IfIndex %{NUMBER:portIfindex:int}\\) has reached %{NUMBER:maximumNumberNeighborsPortMaintain:int}, and no more neighbors can be added.'],
                             'log_explanation': '当邻居数达到最大值的接口收到LLDP报文时，打印本信息', 'log_recommended_action': '无'}]


    elif module == "LOAD":

        if log_type_desc == "BOARD_LOADING":
            pattern_logs = [{'patterns': [
                'Board in chassis %{NUMBER:chassisId:int} slot %{NUMBER:slotId:int} is loading software images.'],
                             'log_explanation': '单板启动过程中，加载启动软件包', 'log_recommended_action': '无'}]

        elif log_type_desc == "LOAD_FAILED":
            pattern_logs = [{'patterns': [
                'Board in chassis %{NUMBER:chassisId:int} slot %{NUMBER:slotId:int} failed to load software images.'],
                             'log_explanation': '单板在启动过程中，加载启动软件包失败',
                             'log_recommended_action': '1.      使用display boot-loader命令查看单板使用的下次启动软件包\n2.      使用dir命令查看启动软件包是否存在。如果不存在或者损坏，请重新获取启动软件包或者设置其它软件包作为该单板的下次启动软件包\n3.      如果仍不能解决，请联系工程师'}]

        elif log_type_desc == "LOAD_FINISHED":
            pattern_logs = [{'patterns': [
                'Board in chassis %{NUMBER:chassisId:int} slot %{NUMBER:slotId:int} has finished loading software images.'],
                             'log_explanation': '单板完成文件加载', 'log_recommended_action': '无'}]


    elif module == "LOGIN":

        if log_type_desc == "LOGIN_FAILED":
            pattern_logs = [{'patterns': ['%{DATA:username} failed to login from %{DATA:lineNameIpAddress}.'],
                             'log_explanation': '用户登录失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "LOGIN_INVALID_USERNAME_PWD":
            pattern_logs = [{'patterns': ['Invalid username or password from %{DATA:userLineNameUserIpAddress}.'],
                             'log_explanation': '用户输入无效的用户名或密码', 'log_recommended_action': '无'}]


    elif module == "LPDT":

        if log_type_desc == "LPDT_LOOPED":
            pattern_logs = [{'patterns': ['A loop was detected on %{DATA:portName}.'],
                             'log_explanation': '接口首次检测到有VLAN发生环路时，环路检测模块会生成该信息', 'log_recommended_action': '检查网络环路'}]

        elif log_type_desc == "LPDT_RECOVERED":
            pattern_logs = [{'patterns': ['All loops were removed on %{DATA:portName}.'],
                             'log_explanation': '接口检测到所有VLAN的环路都消除时，环路检测模块会生成该信息', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "LPDT_VLAN_LOOPED":
            pattern_logs = [{'patterns': ['A loop was detected on %{DATA:portName} in VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '接口检测到一个VLAN发生环路时，环路检测模块会生成该信息',
                             'log_recommended_action': '检查该VLAN的网络环路'}]

        elif log_type_desc == "LPDT_VLAN_RECOVERED":
            pattern_logs = [{'patterns': ['A loop was removed on %{DATA:portName} in VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '接口检测到一个VLAN的环路消除时，环路检测模块会生成该信息', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "LPDT_VSI_LOOPED":
            pattern_logs = [{'patterns': [
                "A loop was detected on VSI %{DATA:param0}'s Ethernet service instance srv%{NUMBER:param1:int} on %{DATA:param2}."],
                             'log_explanation': '接口检测到一个AC口发生环路时，环路检测模块会生成该信息',
                             'log_recommended_action': '检查该VSI的网络环路'}]

        elif log_type_desc == "LPDT_VSI_RECOVERED":
            pattern_logs = [{'patterns': [
                "All loops were removed from VSI %{DATA:param0}'s Ethernet service instance srv%{NUMBER:param1:int} on %{DATA:param2}."],
                             'log_explanation': '接口检测到一个AC口所有的环路消除时，环路检测模块会生成该信息', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "LPDT_VSI_BLOCKFAIL":
            pattern_logs = [{'patterns': [
                "Failed to block %{DATA:param0} that hosts VSI %{DATA:param1}'s Ethernet service instance srv%{NUMBER:param2:int} because of insufficient resources."],
                             'log_explanation': '触发环路检测保护动作后，将端口设置为阻塞失败时生成该信息',
                             'log_recommended_action': '手工处理产生环路的接口'}]


    elif module == "LS":

        if log_type_desc == "LS_ADD_USER_TO_GROUP":
            pattern_logs = [
                {'patterns': ['Admin %{DATA:adminName} added user %{DATA:username} to group %{DATA:userGroupName}.'],
                 'log_explanation': '管理员添加一个用户到一个用户组', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_AUTHEN_FAILURE":
            pattern_logs = [
                {'patterns': ['User %{DATA:param0} from %{DATA:param1} failed authentication. %{DATA:param2}'],
                 'log_explanation': '本地服务器拒绝了一个用户的认证请求', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_AUTHEN_SUCCESS":
            pattern_logs = [
                {'patterns': ['User %{DATA:username} from %{DATA:ipAddress} was authenticated successfully.'],
                 'log_explanation': '本地服务器接受了一个用户的认证请求', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_DEL_USER_FROM_GROUP":
            pattern_logs = [
                {'patterns': ['Admin %{DATA:adminName} delete user %{DATA:username} from group %{DATA:userGroupName}.'],
                 'log_explanation': '管理员将用户从用户组里删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_DELETE_PASSWORD_FAIL":
            pattern_logs = [{'patterns': ['Failed to delete the password for user %{DATA:username}.'],
                             'log_explanation': '删除用户密码失败', 'log_recommended_action': '检查文件系统'}]

        elif log_type_desc == "LS_PWD_ADDBLACKLIST":
            pattern_logs = [{'patterns': [
                'User %{DATA:param0} at %{DATA:param1} was added to the blacklist due to multiple login failures, %{DATA:param2}.'],
                             'log_explanation': '用户多次登录失败后被加入了黑名单', 'log_recommended_action': '检查用户的密码'}]

        elif log_type_desc == "LS_PWD_CHGPWD_FOR_AGEDOUT":
            pattern_logs = [{'patterns': ['User %{DATA:param0} changed the password because it was expired.'],
                             'log_explanation': '用户由于密码已过期而修改了密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_PWD_CHGPWD_FOR_AGEOUT":
            pattern_logs = [{'patterns': ['User %{DATA:param0} changed the password because it was about to expire.'],
                             'log_explanation': '用户由于密码即将过期而修改了密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_PWD_CHGPWD_FOR_COMPOSITION":
            pattern_logs = [
                {'patterns': ['User %{DATA:param0} changed the password because it had an invalid composition.'],
                 'log_explanation': '用户由于密码组合错误而修改了密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_PWD_CHGPWD_FOR_FIRSTLOGIN":
            pattern_logs = [{'patterns': ['User %{DATA:param0} changed the password at the first login.'],
                             'log_explanation': '用户首次登录修改了密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_PWD_CHGPWD_FOR_LENGTH":
            pattern_logs = [{'patterns': ['User %{DATA:param0} changed the password because it was too short.'],
                             'log_explanation': '用户因为密码太短而修改了密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_PWD_MODIFY_FAIL":
            pattern_logs = [{'patterns': [
                'Admin %{DATA:param0} from %{DATA:param1} could not modify the password for user %{DATA:param2}, because %{DATA:param3}.'],
                             'log_explanation': '修改用户密码失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_PWD_MODIFY_SUCCESS":
            pattern_logs = [{'patterns': [
                'Admin %{DATA:adminName} from %{DATA:ipAddress} modify the password for user %{DATA:username} successfully.'],
                             'log_explanation': '管理员成功修改了用户密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_REAUTHEN_FAILURE":
            pattern_logs = [{'patterns': ['User %{DATA:username} from %{DATA:ipAddress} failed reauthentication.'],
                             'log_explanation': '用户再次认证失败', 'log_recommended_action': '检查旧密码'}]

        elif log_type_desc == "LS_UPDATE_PASSWORD_FAIL":
            pattern_logs = [{'patterns': ['Failed to update the password for user %{DATA:username}.'],
                             'log_explanation': '为用户更新密码失败', 'log_recommended_action': '检查文件系统'}]

        elif log_type_desc == "LS_USER_CANCEL":
            pattern_logs = [
                {'patterns': ['User %{DATA:username} from %{DATA:ipAddress} cancelled inputting the password.'],
                 'log_explanation': '用户取消输入密码或者没有在90秒内输入密码', 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_USER_PASSWORD_EXPIRE":
            pattern_logs = [
                {'patterns': ["User %{DATA:username}'s login idle timer timed out."], 'log_explanation': '用户登录空闲时间超时',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "LS_USER_ROLE_CHANGE":
            pattern_logs = [
                {'patterns': ['Admin %{DATA:param0} %{DATA:param1} the user role %{DATA:param2} for %{DATA:param3}.'],
                 'log_explanation': '管理员修改了用户的用户角色', 'log_recommended_action': '无'}]


    elif module == "PWDCTL":

        if log_type_desc == "FAILEDTOWRITEPWD":
            pattern_logs = [
                {'patterns': ['Failed to write the password records to file.'], 'log_explanation': '设备无法将用户密码写入密码记录文件',
                 'log_recommended_action': '请检查设备文件系统存储空间是否充足'}]

        elif log_type_desc == "ADDBLACKLIST":
            pattern_logs = [{'patterns': ['%{DATA:username} was added to the blacklist for failed login attempts.'],
                             'log_explanation': '因为用户输入密码错误，用户登录设备失败，被加入密码控制黑名单', 'log_recommended_action': '无'}]

        elif log_type_desc == "CNAHGEPASSWORD":
            pattern_logs = [
                {'patterns': ['%{DATA:username} changed the password because %{DATA:theReasonsChangingPassword}.'],
                 'log_explanation': '由于某种原因，用户改变用户密码。例如该用户的账户第一次登录设备', 'log_recommended_action': '无'}]

        elif log_type_desc == "FAILEDTOOPENFILE":
            pattern_logs = [
                {'patterns': ['Failed to open the password file.'], 'log_explanation': '因文件系统异常导致创建或打开*.dat文件失败',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "NOENOUGHSPACE":
            pattern_logs = [{'patterns': ['Not enough free space on the storage media where the file is located.'],
                             'log_explanation': '配置失败，因为*.dat文件所在介质（Flash或CF卡等）存储空间不足',
                             'log_recommended_action': '请检查设备文件系统存储空间是否充足'}]

        elif log_type_desc == "UPDATETIME":
            pattern_logs = [
                {'patterns': ['Last login time updated after clock update.'], 'log_explanation': '用户最近登录时间已同步更新',
                 'log_recommended_action': '无'}]


    elif module == "LSPV":

        if log_type_desc == "LSPV_PING_STATIS_INFO":
            pattern_logs = [{'patterns': [
                'Ping statistics for %{DATA:fec}: %{NUMBER:numberEchoRequestsSent:int} packets transmitted, %{NUMBER:numberEchoRepliesReceived:int} packets received, %{DATA:percentageNon-repliedPacketsTotalRequests}% packets loss, round-trip min/avg/max = %{NUMBER:minimumRound-tripDelay:int}/%{NUMBER:averageRound-tripDelay:int}/%{NUMBER:maximumRound-tripDelay:int} ms.'],
                             'log_explanation': '执行ping mpls命令，触发该日志。日志显示ping的统计信息',
                             'log_recommended_action': '如果没有收到应答报文，检测到LSP隧道或者PW的连通性'}]


    elif module == "MAC":

        if log_type_desc == "MAC_DRIVER_ADD_ENTRY":
            pattern_logs = [{'patterns': [
                'Driver failed to add MAC address entry: MAC address=%{DATA:macAddress}, VLAN=%{NUMBER:vlanId:int}, State=%{NUMBER:entryTypeNumber:int}, interface=%{DATA:interfaceTypeInterfaceNumber}.'],
                             'log_explanation': '在接口GigabitEthernet1/0/1上添加OpenFlow类型MAC地址失败，MAC地址为1-1-1，所属VLAN为VLAN 1',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_PROTOCOLPKT_NORES_GLOBAL":
            pattern_logs = [{'patterns': [
                'The card does not have enough hardware resources to send protocol packets destined for %{DATA:macAddress} to the CPU for %{DATA:protocolType},'],
                             'log_explanation': '单板硬件资源不足导致协议报文上送CPU失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_PROTOCOLPKT_NORES_PORT":
            pattern_logs = [{'patterns': [
                'The card does not have enough hardware resources to send protocol packets destined for %{DATA:macAddress} to the CPU for %{DATA:protocolType} on %{DATA:interfaceName}.'],
                             'log_explanation': '单板硬件资源不足导致接口上的协议报文上送CPU失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_PROTOCOLPKT_NORES_VLAN":
            pattern_logs = [{'patterns': [
                'The card does not have enough hardware resources to send protocol packets destined for %{DATA:macAddress} to the CPU for %{DATA:protocolType} in VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '单板硬件资源不足导致VLAN内的协议报文上送CPU失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_TABLE_FULL_GLOBAL":
            pattern_logs = [{'patterns': [
                'The number of MAC address entries exceeded the maximum number %{NUMBER:maximumNumberMacAddresses:int}.'],
                             'log_explanation': '全局MAC地址表中的表项数量超过了允许的最大数量', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_TABLE_FULL_PORT":
            pattern_logs = [{'patterns': [
                'The number of MAC address entries exceeded the maximum number %{NUMBER:maximumNumberMacAddresses:int} for interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口对应的MAC地址表中的表项数量超过了允许的最大数量', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_TABLE_FULL_VLAN":
            pattern_logs = [{'patterns': [
                'The number of MAC address entries exceeded the maximum number %{NUMBER:maximumNumberMacAddresses:int} in VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': 'VLAN对应的MAC地址表中的表项数量超过了允许的最大数量', 'log_recommended_action': '无'}]

        elif log_type_desc == "MAC_VLAN_LEARNLIMIT_NORESOURCE":
            pattern_logs = [{'patterns': [
                'The card does not have enough hardware resources to set MAC learning limit for VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '单板硬件资源不足导致无法配置VLAN内允许学习的最大MAC地址数量', 'log_recommended_action': '无'}]

        elif log_type_desc == " MAC_VLAN_LEARNLIMIT_NOTSUPPORT":
            pattern_logs = [
                {'patterns': ['The card does not support setting MAC learning limit for VLAN %{NUMBER:vlanId:int}.'],
                 'log_explanation': '单板不支持配置VLAN内允许学习的最大MAC地址数量', 'log_recommended_action': '无'}]


    elif module == "MACA":

        if log_type_desc == "MACA_ENABLE_NOT_EFFECTIVE":
            pattern_logs = [{'patterns': [
                'MAC authentication is enabled but is not effective on interface %{DATA:interfaceTypeNumber}.'],
                             'log_explanation': 'MAC地址认证配置在接口上不生效，因为该接口不支持MAC地址认证',
                             'log_recommended_action': '关闭接口上的MAC地址认证'}]

        elif log_type_desc == "MACA_LOGIN_FAILURE":
            pattern_logs = [{'patterns': ['User failed MAC authentication. Reason: %{DATA:failureCause}.'],
                             'log_explanation': '用户MAC地址认证失败', 'log_recommended_action': '查看失败原因并修改相关配置'}]

        elif log_type_desc == "MACA_LOGIN_SUCC":
            pattern_logs = [
                {'patterns': ['User passed MAC authentication and came online.'], 'log_explanation': 'MAC地址认证成功',
                 'log_recommended_action': '无'},
                {'patterns': ['The user that failed MAC authentication passed open authentication and came online.'],
                 'log_explanation': 'MAC地址认证失败但通过开放认证模式成功上线', 'log_recommended_action': '无'}]

        elif log_type_desc == "MACA_LOGOFF":
            pattern_logs = [{'patterns': ['MAC authentication user was logged off.'], 'log_explanation': 'MAC地址认证用户下线',
                             'log_recommended_action': '查看下线原因或进行后续操作'},
                            {'patterns': ['MAC authentication open user was logged off.'],
                             'log_explanation': 'MAC地址认证open用户下线', 'log_recommended_action': '查看下线原因或进行后续操作'}]


    elif module == "MACSEC":

        if log_type_desc == "MACSEC_MKA_KEEPALIVE_TIMEOUT":
            pattern_logs = [{'patterns': [
                'The live peer with SCI %{DATA:sci} and CKN %{DATA:ckn} aged out on interface %{DATA:interfaceName}.'],
                             'log_explanation': '本端参与者和对端参与者相互学习到后，本端参与者为对端参与者启动一个保活定时器。如果本端参与者在保活定时器超时的时间内没有收到对端参与者的MKA报文，则将对端参与者的信息从本端删除掉，并触发该日志',
                             'log_recommended_action': '检查本端参与者和对端参与者所在链路是否故障，如果链路故障，则请恢复链路'}]

        elif log_type_desc == "MACSEC_MKA_PRINCIPAL_ACTOR":
            pattern_logs = [{'patterns': [
                'The actor with CKN %{DATA:ckn} became principal actor on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口上可能存在多个行动者，具有最高优先级的Key Server的行动者被选举为主要行动者，触发该日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MACSEC_MKA_SAK_REFRESH":
            pattern_logs = [{'patterns': ['The SAK has been refreshed on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口上的参与者派生出或接收到新的SAK时，触发该日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "MACSEC_MKA_SESSION_REAUTH":
            pattern_logs = [{'patterns': [
                'The MKA session with CKN %{DATA:ckn} was re-authenticated on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口进行802.1X重认证时，触发该日志。重认证过程中，参与者接收到新的CAK，并使用它重建会话',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MACSEC_MKA_SESSION_SECURED":
            pattern_logs = [
                {'patterns': ['The MKA session with CKN %{DATA:ckn} was secured on interface %{DATA:interfaceName}.'],
                 'log_explanation': '接口上的MKA会话采用密文通信方式。触发该日志的原因可能包括：\n·          MKA会话由明文通信切换为密文通信\n·          Key Server和它对端的接口都支持MACsec功能，且两端至少有一个期望MACsec保护的情况下，两端协商出新的会话',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "MACSEC_MKA_SESSION_START":
            pattern_logs = [
                {'patterns': ['The MKA session with CKN %{DATA:ckn} started on interface %{DATA:interfaceName}.'],
                 'log_explanation': 'MKA会话协商开始。触发该日志的原因可能包括：\n·          使能MKA功能后，有新的可用CAK\n·          用户重建MKA会话\n·          协商会话失败的接口收到新的MKA报文',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "MACSEC_MKA_SESSION_STOP":
            pattern_logs = [
                {'patterns': ['The MKA session with CKN %{DATA:ckn} stopped on interface %{DATA:interfaceName}.'],
                 'log_explanation': 'MKA会话终止。触发该日志的原因可能包括：\n·          用户删除或重建了接口的MKA会话\n·          MKA会话所在链路故障',
                 'log_recommended_action': '使用display mka session命令查看会话是否存在。如果会话不存在且不是用户删除的，则需要检查会话所在链路是否故障。如果链路故障，则请恢复链路'}]

        elif log_type_desc == "MACSEC_MKA_SESSION_UNSECURED":
            pattern_logs = [{'patterns': [
                'The MKA session with CKN %{DATA:ckn} was not secured on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口上的MKA会话采用明文通信方式。输出该日志的触发条件可能包括：\n·          MKA会话由密文通信切换为明文通信\n·          Key Server和它对端的接口未能都支持MACsec功能，或两端均未期望MACsec保护的情况下，两端协商出新的会话',
                             'log_recommended_action': '如果用户希望会话采用密文通信方式，则请先确认Key Server和它对端的接口都支持MACsec功能，再确认两个接口中至少有一个期望MACsec保护，只有两个条件都成立，会话才能采用密文通信方式'}]


    elif module == "MBFD":

        if log_type_desc == "MBFD_TRACEROUTE_FAILURE":
            pattern_logs = [{'patterns': ['%{DATA:lspInformation} is failed. \\(%{DATA:reasonLspFailure}.\\)'],
                             'log_explanation': '通过周期性Traceroute功能检测LSP或MPLS TE隧道时，如果收到带有不合法返回代码的应答，则打印本日志信息，说明LSP或者MPLS TE隧道出现了故障',
                             'log_recommended_action': '检查LSP或者MPLS TE隧道的配置情况'}]


    elif module == "MBUF":

        if log_type_desc == "MBUF_DATA_BLOCK_CREATE_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to create an MBUF data block because of insufficient memory. Failure count: %{NUMBER:failureCount:int}.'],
                             'log_explanation': '当申请MBUF数据块失败时，输出该日志。为避免该日志输出过于频繁，本次申请MBUF数据块失败距上次申请MBUF数据块失败间隔大于等于一分钟时，才会输出该日志',
                             'log_recommended_action': '1.      在Probe视图下执行display system internal kernel memory pool | include mbuf命令查询已申请的MBUF数据块的数量\n2.      在系统视图下执行display memory命令查询系统内存总量\n3.      将“已申请的MBUF数据块的数量”和“系统内存总量”比较，判断是否已申请的MBUF数据块过多导致申请失败\n·          如果不是，则通过其他内存管理命令查询出占用内存较多的模块\n·          如果是，则继续通过Probe视图下的display system internal mbuf socket statistics命令查询Socket申请的MBUF数据块的数量，对比已申请的MBUF数据块的数量，判断是否某个进程缓存在Socket缓冲区中的MBUF数据块过多\n¡  如果是，则进一步分析进程不能及时释放Socket缓冲区中的MBUF数据块的原因\n¡  如果不是，则需要通过其他手段找出申请大量MBUF数据块的真正原因'}]


    elif module == "MDC":

        if log_type_desc == "MDC_CREATE":
            pattern_logs = [{'patterns': ['MDC %{NUMBER:mdcId:int} was created.'], 'log_explanation': 'MDC成功创建',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MDC_CREATE_ERR":
            pattern_logs = [{'patterns': ['Failed to create MDC %{NUMBER:mdcId:int} for insufficient resources.'],
                             'log_explanation': '备用主控板启动时会从主用主控板获取所有已创建的MDC的信息，并在备用主控板创建同样的MDC。如果备用主控板因为资源限制无法创建该MDC，则输出此日志信息。MDC进驻备用主控板失败，无法在该备用主控板上提供服务',
                             'log_recommended_action': '1.      使用display mdc resource命令查询新插入的备用主控板的CPU、内存空间和磁盘空间\n2.      增加备用主控板的内存或减少磁盘使用，以保证新MDC可创建\n3.      使用undo mdc命令删除该MDC，或者换一块资源足够的主控板作为备用主控板'}]

        elif log_type_desc == "MDC_DELETE":
            pattern_logs = [{'patterns': ['MDC %{NUMBER:mdcId:int} was deleted.'], 'log_explanation': 'MDC成功删除',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MDC_KERNEL_EVENT_TOOLONG":
            pattern_logs = [{'patterns': [
                '%{DATA:objectType} %{NUMBER:mdcIdContextId:int} kernel event in sequence %{DATA:kernelEventPhase} function %{DATA:addressFunctionCorrespondingKernelEvent} failed to finish within %{NUMBER:timeDuration:int} minutes.'],
                             'log_explanation': '某内核事件在长时间内未完成',
                             'log_recommended_action': '1.      重启单板，尝试恢复\n2.      联系工程师分析解决'}]

        elif log_type_desc == "MDC_LICENSE_EXPIRE":
            pattern_logs = [{'patterns': ["The MDC feature's license will expire in %{NUMBER:numberDays:int} days."],
                             'log_explanation': 'MDC License将在指定天数后失效', 'log_recommended_action': '安装新的License'}]

        elif log_type_desc == "MDC_NO_FORMAL_LICENSE":
            pattern_logs = [{'patterns': ['The feature MDC has no formal license.'],
                             'log_explanation': '备用主控板变为主用主控板了，但是新主用主控板没有安装MDC License。系统会给新主用主控板一个MDC试用期。试用期过期，如果用户还没有给新主用主控板安装License，则不能继续使用MDC特性',
                             'log_recommended_action': '安装正式MDC License'}]

        elif log_type_desc == "MDC_NO_LICENSE_EXIT":
            pattern_logs = [{'patterns': ['The MDC feature is being disabled, because it has no license.'],
                             'log_explanation': 'MDC特性被禁用，因为MDC License过期或者被卸载了',
                             'log_recommended_action': '安装MDC License'}]

        elif log_type_desc == "MDC_OFFLINE":
            pattern_logs = [{'patterns': ['MDC %{NUMBER:mdcId:int} is offline now.'], 'log_explanation': 'MDC停用了',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MDC_ONLINE":
            pattern_logs = [{'patterns': ['MDC %{NUMBER:mdcId:int} is online now.'], 'log_explanation': 'MDC启用了',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "MDC_STATE_CHANGE":
            pattern_logs = [{'patterns': ['MDC %{NUMBER:param0:int} status changed to %{DATA:param1}.'],
                             'log_explanation': 'MDC状态发生了变化', 'log_recommended_action': '无'}]


    elif module == "MFIB":

        if log_type_desc == "MFIB_MEM_ALERT":
            pattern_logs = [
                {'patterns': ['MFIB process received system memory alert %{DATA:typeMemoryAlertEvent} event.'],
                 'log_explanation': 'MFIB模块收到了系统发出的内存告警事件',
                 'log_recommended_action': '当超过各级内存门限时，检查系统内存占用情况，对占用内存较多的模块进行调整，尽量释放可用内存'}]


    elif module == "MGROUP":

        if log_type_desc == "MGROUP_APPLY_SAMPLER_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply the sampler for mirroring group %{NUMBER:mirroringGroupId:int}, because the sampler resources are insufficient.'],
                             'log_explanation': '采样器资源不足时，新镜像组引用采样器失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "MGROUP_RESTORE_CPUCFG_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to restore configuration for mirroring CPU of %{DATA:slotNumber} in mirroring group %{NUMBER:mirroringGroupId:int}, because %{DATA:failureReason}'],
                             'log_explanation': '当单板上的CPU用作镜像组的源CPU时，在单板拔出阶段，配置发生变化，单板再插入时，可能会引起镜像组源CPU的配置恢复失败',
                             'log_recommended_action': '排查配置恢复失败的原因，如果是由于系统不支持变化的配置，删除不支持的配置，重新配置镜像组的源CPU'}]

        elif log_type_desc == "MGROUP_RESTORE_GROUP_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to restore configuration for mirroring group %{NUMBER:mirroringGroupId:int}, because %{DATA:failureReason}'],
                             'log_explanation': '设备启动后，因为镜像资源不足，导致镜像组的配置恢复失败',
                             'log_recommended_action': '流镜像和端口镜像使用相同的镜像资源。当设备整机重启时，优先恢复流镜像配置，再恢复端口镜像配置。请删除不需要的镜像配置释放资源，然后重新配置恢复失败的镜像组'}]

        elif log_type_desc == "MGROUP_RESTORE_IFCFG_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to restore configuration for interface %{DATA:param0} in mirroring group %{NUMBER:param1:int}, because %{DATA:param2}'],
                             'log_explanation': '当单板上的接口用作镜像组的源端口时，在单板拔出阶段，配置发生变化，单板再插入时，可能会引起镜像组源端口的配置恢复失败',
                             'log_recommended_action': '排查配置恢复失败的原因，如果是由于系统不支持变化的配置，删除不支持的配置，重新配置镜像组的源端口'}]

        elif log_type_desc == "MGROUP_SYNC_CFG_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to restore configuration for mirroring group %{NUMBER:mirroringGroupId:int} in %{DATA:slotNumber}, because %{DATA:failureReason}'],
                             'log_explanation': '当向单板同步完整的镜像组配置时，由于单板资源不足，引起配置恢复失败',
                             'log_recommended_action': '删除配置恢复失败的镜像组'}]


    elif module == "MPLS":

        if log_type_desc == "MPLS_HARD_RESOURCE_NOENOUGH":
            pattern_logs = [{'patterns': ['No enough hardware resource for MPLS.'], 'log_explanation': 'MPLS硬件资源不足',
                             'log_recommended_action': '请检查是否生成了当前业务不需要的大量LSP，是则配置获调整标签分发协议的LSP触发策略、标签通告策略、标签接受策略，以过滤掉不需要的LSP'}]

        elif log_type_desc == "MPLS_HARD_RESOURCE_RESTORE":
            pattern_logs = [{'patterns': ['Hardware resources for MPLS are restored.'], 'log_explanation': 'MPLS硬件资源恢复',
                             'log_recommended_action': '无'}]


    elif module == "MTLK":

        if log_type_desc == "MTLK_UPLINK_STATUS_CHANGE":
            pattern_logs = [{'patterns': [
                'The uplink of monitor link group %{NUMBER:monitorLinkGroupId:int} is %{DATA:monitorLinkGroupStatus}.'],
                             'log_explanation': 'Monitor Link组上行链路up或down', 'log_recommended_action': '检查故障链路'}]


    elif module == "SESSION":

        if log_type_desc == "SESSION_IPV4_FLOW":
            pattern_logs = [{'patterns': [
                'Protocol\\(1001\\)=%{DATA:protocolType};SrcIPAddr\\(1003\\)=%{IP:sourceIpAddress};SrcPort\\(1004\\)=%{NUMBER:sourcePortNumber:int};NATSrcIPAddr\\(1005\\)=%{IP:sourceIpAddressTranslation};NATSrcPort\\(1006\\)=%{NUMBER:sourcePortNumberTranslation:int};DstIPAddr\\(1007\\)=%{IP:destinationIpAddress};DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int};NATDstIPAddr\\(1009\\)=%{IP:destinationIpAddressTranslation};NATDstPort\\(1010\\)=%{NUMBER:destinationPortNumberTranslation:int};InitPktCount\\(1044\\)=%{NUMBER:totalNumberInboundPackets:int};InitByteCount\\(1046\\)=%{NUMBER:totalNumberInboundBytes:int};RplyPktCount\\(1045\\)=%{NUMBER:totalNumberOutboundPackets:int};RplyByteCount\\(1047\\)=%{NUMBER:totalNumberOutboundBytes:int};RcvVPNInstance\\(1042\\)=%{DATA:sourceVpnInstanceName};SndVPNInstance\\(1043\\)=%{DATA:destinationVpnInstanceName};RcvDSLiteTunnelPeer\\(1040\\)=%{DATA:sourceDs-liteTunnel};SndDSLiteTunnelPeer\\(1041\\)=%{DATA:destinationDs-liteTunnel};BeginTime_e\\(1013\\)=%{DATA:timeSessionCreated};EndTime_e\\(1014\\)=%{DATA:timeSessionRemoved};Event\\(1048\\)=\\(%{NUMBER:eventType:int}\\)%{DATA:eventDescription};'],
                             'log_explanation': '创建、删除IPv4会话时会发送该日志\nIPv4会话过程中会定时发送该日志\nIPv4会话的流量或时间达到指定的阈值时会发送该日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SESSION_IPV6_FLOW":
            pattern_logs = [{'patterns': [
                'Protocol\\(1001\\)=%{DATA:protocolType};SrcIPv6Addr\\(1036\\)=%{IP:sourceIpv6Address};SrcPort\\(1004\\)=%{NUMBER:sourcePortNumber:int};DstIPv6Addr\\(1037\\)=%{IP:destinationIpAddress};DstPort\\(1008\\)=%{NUMBER:destinationPortNumber:int};InitPktCount\\(1044\\)=%{NUMBER:totalNumberInboundPackets:int};InitByteCount\\(1046\\)=%{NUMBER:totalNumberInboundBytes:int};RplyPktCount\\(1045\\)=%{NUMBER:totalNumberOutboundPackets:int};RplyByteCount\\(1047\\)=%{NUMBER:totalNumberOutboundBytes:int};RcvVPNInstance\\(1042\\)=%{DATA:sourceVpnInstanceName};SndVPNInstance\\(1043\\)=%{DATA:destinationVpnInstanceName};BeginTime_e\\(1013\\)=%{DATA:timeSessionCreated};EndTime_e\\(1014\\)=%{DATA:timeSessionRemoved};Event\\(1048\\)=\\(%{NUMBER:eventType:int}\\)%{DATA:eventDescription};'],
                             'log_explanation': '创建、删除IPv6会话时会发送该日志\nIPv6会话过程中会定时发送该日志\nIPv6会话的流量或时间达到指定的阈值时会发送该日志',
                             'log_recommended_action': '无'}]


    elif module == "ND":

        if log_type_desc == "ND_COMMONPROXY_ENABLE_FAILED":
            pattern_logs = [{'patterns': ['Failed to enable common ND proxy on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口下开启普通ND代理失败。如果非主控板的接口下开启普通ND代理失败，则在对应的接口板上打印该日志信息',
                             'log_recommended_action': '·          检查设备相应单板是否支持本功能\n·          确认设备的硬件资源是否充足'}]

        elif log_type_desc == "ND_CONFLICT":
            pattern_logs = [
                {'patterns': ['%{DATA:param0} is inconsistent.'], 'log_explanation': '设备收到一个路由通告消息，导致与邻居路由器上的配置不一致',
                 'log_recommended_action': '检查并保证设备与邻居路由器上的配置一致'}]

        elif log_type_desc == "ND_DUPADDR":
            pattern_logs = [{'patterns': [
                'Duplicate address: %{DATA:ipv6AddressAssignedInterface} on the interface %{DATA:nameInterface}.'],
                             'log_explanation': '分配给该接口的地址已经被其他设备使用', 'log_recommended_action': '分配一个新的IPv6地址'}]

        elif log_type_desc == "ND_HOST_IP_CONFLICT":
            pattern_logs = [{'patterns': [
                'The host %{DATA:ipv6GlobalUnicastAddressHost} connected to interface %{DATA:nameInterface} cannot communicate correctly, because it uses the same IPv6 address as the host connected to interface %{DATA:nameInterface}.'],
                             'log_explanation': '分配给该接口的地址已经被其他设备使用',
                             'log_recommended_action': '分配一个新的IPv6地址。如果非法，需要断开该主机网络'}]

        elif log_type_desc == "ND_LOCALPROXY_ENABLE_FAILED":
            pattern_logs = [{'patterns': ['Failed to enable local ND proxy on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口下开启本地ND代理失败。如果非主控板的接口下开启本地ND代理失败，则在对应的接口板上打印该日志信息',
                             'log_recommended_action': '·          检查设备相应单板是否支持本功能\n·          确认设备的硬件资源是否充足'}]

        elif log_type_desc == "ND_MAC_CHECK":
            pattern_logs = [{'patterns': [
                'Packet received on interface %{DATA:receivingInterfaceNdPacket} was dropped because source MAC %{DATA:sourceMacAddressEthernetFrameHeaderNdPacket} was inconsistent with link-layer address %{DATA:sourceLink-layerAddressNdPacket}.'],
                             'log_explanation': 'ipv6 nd mac-check enable命令用来在网关设备上开启ND协议报文源MAC地址一致性检查功能。在网关开启此功能后，会对接收的ND协议报文进行检查，如果ND协议报文中的源MAC地址和源链路层选项地址中的MAC地址不同，则丢弃该报文。若使用ipv6 nd check log enable命令来开启ND日志信息功能，会有相关的log信息输出',
                             'log_recommended_action': '检查链路层源MAC对应主机的合法性'}]

        elif log_type_desc == "ND_NETWORKROUTE_DUPLICATE":
            pattern_logs = [{'patterns': [
                'Prefix %{DATA:ipv6AddressPrefix} of the IPv6 ND network route matches different ports: %{DATA:interfaceName} and %{DATA:interfaceName}.'],
                             'log_explanation': '使用ipv6 nd route-direct prefix convert-length命令配置匹配指定IPv6前缀的ND表项生成网段路由的前缀长度后，如果根据不同的ND表项（与邻居相连的二层端口不同、但是与邻居相连的接口所属的VLAN相同）生成相同的网段路由，则输出本日志',
                             'log_recommended_action': '检查网络配置，根据实际需求修改网络配置'}]

        elif log_type_desc == "ND_RAGUARD_DROP":
            pattern_logs = [{'patterns': [
                'Dropped RA messages with the source IPv6 address %{DATA:ipv6SourceIpAddressDroppedRaMessages} on interface %{DATA:interfaceNameRaMessagesDropped}. %{DATA:totalNumberDroppedRaMessagesInterface} messages dropped in total on the interface.'],
                             'log_explanation': 'RA Guard检测到攻击，丢弃相应的报文并提示日志信息', 'log_recommended_action': '检查报文源是否合法'}]

        elif log_type_desc == "ND_RATE_EXCEEDED":
            pattern_logs = [{'patterns': [
                'The ND packet rate \\(%{NUMBER:ndPacketRate:int} pps\\) exceeded the rate limit \\(%{NUMBER:ndLimitRate:int} pps\\) on interface %{DATA:interfaceName} in most recent %{NUMBER:intervalTime:int} seconds.'],
                             'log_explanation': '在此前的一段时间内，接口接收ND报文速率超过了接口的ND报文限速值',
                             'log_recommended_action': '检查发送ND报文的主机是否合法'}]

        elif log_type_desc == "ND_RATELIMIT_NOTSUPPORT":
            pattern_logs = [{'patterns': ['ND packet rate limit is not support on slot %{NUMBER:slotNumber:int}.',
                                          'ND packet rate limit is not support on chassis %{NUMBER:chassisNumber:int} slot %{NUMBER:slotNumber:int}.'],
                             'log_explanation': '指定的slot上不支持ND报文限速功能', 'log_recommended_action': '无需处理'}]

        elif log_type_desc == "ND_VLAN_REDIRECT_NORESOURCE":
            pattern_logs = [{'patterns': ['Not enough resources to complete the operation.'],
                             'log_explanation': '下发VLAN规则失败，原因是驱动资源不足', 'log_recommended_action': '释放设备驱动资源，重新下发'}]

        elif log_type_desc == "ND_SNOOPING_LEARN_ALARM":
            pattern_logs = [{'patterns': [
                'The total number of ND snooping entries learned in all VLANs reached or exceeded the alarm threshold.'],
                             'log_explanation': '所有VLAN学习的总的ND Snooping表项数达到或超过告警阈值',
                             'log_recommended_action': '检查是否有ND攻击'}]

        elif log_type_desc == "ND_SNOOPING_LEARN_ALARM_RECOVER":
            pattern_logs = [{'patterns': [
                'The total number of ND snooping entries learned in all VLANs dropped below the alarm threshold.'],
                             'log_explanation': '所有VLAN学习的总的ND Snooping表项数降低到告警阈值以下', 'log_recommended_action': '无'}]

        elif log_type_desc == "ND_USER_DUPLICATE_IPV6ADDR":
            pattern_logs = [{'patterns': [
                'Detected a user IPv6 address conflict. New user \\(MAC %{DATA:macAddressNewUser}, SVLAN %{DATA:svlanNewUser}, CVLAN %{DATA:cvlanNewUser}\\) on interface %{DATA:nameInterfaceConnectedNewUser} and old user \\(MAC %{DATA:macAddressOldUser}, SVLAN %{DATA:svlanOldUser}, CVLAN %{DATA:cvlanOldUser}\\) on interface %{DATA:nameInterfaceConnectedOldUser} were using the same IPv6 address %{IPV6:ipv6AddressUser}.'],
                             'log_explanation': '使用ipv6 nd user-ip-conflict record enable命令开启ND记录终端用户间IPv6地址冲突功能后，如果设备检测到冲突，则输出本日志',
                             'log_recommended_action': '排查所有终端用户的IPv6地址，解决IPv6地址冲突问题'}]

        elif log_type_desc == "ND_USER_MOVE":
            pattern_logs = [{'patterns': [
                'Detected a user \\(IPv6 address %{IPV6:ipv6AddressUser}, MAC address %{DATA:macAddressUser}\\) moved to another interface. Before user move: interface %{DATA:interfaceNameMigration}, SVLAN %{DATA:oldSvlanUser}, CVLAN %{DATA:oldCvlanUser}. After user move: interface %{DATA:interfaceNameMigration}, SVLAN %{DATA:newSvlanUser}, CVLAN %{DATA:newCvlanUser}.'],
                             'log_explanation': '使用ipv6 nd user-move record enable命令开启ND记录终端用户端口迁移功能后，如果设备检测到终端用户在接口间迁移，则输出本日志',
                             'log_recommended_action': '使用display ipv6 nd user-move record命令查看终端用户端口迁移表项信息，确认迁移是否合理'}]

        elif log_type_desc == "ND_USER_OFFLINE":
            pattern_logs = [{'patterns': [
                'Detected a user \\(IPv6 address %{IPV6:ipv6AddressOfflineUser}, MAC address %{DATA:macAddressOfflineUser}\\) was offline from interface %{DATA:nameInterfaceConnectedOfflineUser}.'],
                             'log_explanation': '使用ipv6 nd online-offline-log enable命令开启ND输出终端用户上下线日志功能后，如果设备检测到终端用户下线，则输出本日志',
                             'log_recommended_action': '无需处理'}]

        elif log_type_desc == "ND_USER_ONLINE":
            pattern_logs = [{'patterns': [
                'Detected a user \\(IPv6 address %{IPV6:ipv6AddressOnlineUser}, MAC address %{DATA:macAddressOnlineUser}\\) was online on interface %{DATA:nameInterfaceConnectedOnlineUser}.'],
                             'log_explanation': '使用ipv6 nd online-offline-log enable命令开启ND输出终端用户上下线日志功能后，如果设备检测到终端用户上线，则输出本日志',
                             'log_recommended_action': '检查上线用户是否是合法用户'}]


    elif module == "XMLSOAP":

        if log_type_desc == "CLI":
            pattern_logs = [{'patterns': [
                'User \\(%{DATA:param0}, %{DATA:param1}%{DATA:param2}\\) performed an CLI operation: %{DATA:param3} operation result=%{DATA:param4}%{DATA:param5}'],
                             'log_explanation': 'CLI配置执行完毕后，输出CLI的执行结果', 'log_recommended_action': '无'}]

        elif log_type_desc == "EDIT-CONFIG":
            pattern_logs = [{'patterns': [
                'User \\(%{DATA:param0}, %{DATA:param1}%{DATA:param2}\\)%{DATA:param3} operation=%{DATA:param4} %{DATA:param5} %{DATA:param6}, result=%{DATA:param7}. No attributes.',
                'User \\(%{DATA:param8}, %{DATA:param9},%{DATA:param10}\\),%{DATA:param11} operation=%{DATA:param12} %{DATA:param13} %{DATA:param14}, result=%{DATA:param15}. Attributes: %{DATA:param16}.'],
                             'log_explanation': '按NETCONF行操作输出日志，用户下发一次NETCONF操作，设备输出该操作中每个请求行操作的日志\n仅action和set操作支持输入该日志',
                             'log_recommended_action': '无'}]


    elif module == "NETCONF":

        if log_type_desc == "NETCONF_MSG_DEL":
            pattern_logs = [
                {'patterns': ['A NETCONF message was dropped. Reason: Packet size exceeded the upper limit.'],
                 'log_explanation': '来自NETCONF over SSH客户端或XML视图的NETCONF请求报文由于其大小超过设备支持的上限而被丢弃',
                 'log_recommended_action': '1.      减小发往设备的单个NETCONF请求报文的大小，例如删除报文中的空格、换行、制表符等占位字符\n2.      如果报文仍然过大，可以拆分NETCONF请求并分别封装后再发送给设备，建议联系技术支持'}]


    elif module == "XMLCFG":

        if log_type_desc == "THREAD":
            pattern_logs = [{'patterns': ['Maximum number of NETCONF threads already reached.'],
                             'log_explanation': 'NETCONF线程数达到上限', 'log_recommended_action': 'NETCONF线程数达到上限，请稍后重试'}]


    elif module == "NQA":

        if log_type_desc == "NQA_ENTRY_PROBE_RESULT":
            pattern_logs = [{'patterns': [
                'Reaction entry %{DATA:idNqaReactionEntry} of NQA entry admin-name %{DATA:adminNameNqaEntry} operation-tag %{DATA:operationTagNqaEntry}: %{DATA:testResult}.'],
                             'log_explanation': 'NQA客户端的阈值告警监测对象的数值与上次探测相比发生了变化，触发告警或者告警解除',
                             'log_recommended_action': '·          如果测试成功，无需处理\n·          如果测试失败，请检查网络环境'}]

        elif log_type_desc == "NQA_LOG_UNREACHABLE":
            pattern_logs = [{'patterns': ['Server %{DATA:ipAddressNqaServer} unreachable.'],
                             'log_explanation': 'NQA客户端检测到NQA服务器不可达', 'log_recommended_action': '检查网络环境'}]

        elif log_type_desc == "NQA_START_FAILURE":
            pattern_logs = [{'patterns': [
                'NQA entry \\(%{DATA:adminNameNqaOperation}-%{DATA:operationTagNqaOperation}\\): %{DATA:failureReason}'],
                             'log_explanation': 'NQA测试下发驱动执行时，失败',
                             'log_recommended_action': '·          检查配置参数进行修改并重新启动测试\n·          联系技术支持'}]

        elif log_type_desc == " NQA_TWAMP_LIGHT_PACKET_INVALID":
            pattern_logs = [{'patterns': [
                'NQA TWAMP Light test session %{NUMBER:testSessionId:int} index %{NUMBER:serialNumberStatisticsData:int}: The number of packets captured for statistics collection is invalid.'],
                             'log_explanation': '统计的探测帧数量异常，本次探测统计结果不计入统计计数',
                             'log_recommended_action': '检查NQA TWAMP-light测试配置，可能原因为：配置的统计周期小于发送报文的周期'}]

        elif log_type_desc == "NQA_TWAMP_LIGHT_REACTION":
            pattern_logs = [{'patterns': [
                'NQA TWAMP Light test session %{NUMBER:testSessionId:int} reaction entry %{NUMBER:reactionEntryId:int}: Detected continual violation of the %{DATA:reactionEntryType} %{DATA:thresholdViolationValue} threshold for a threshold violation monitor time of %{NUMBER:statisticsCollectionInterval:int} ms.'],
                             'log_explanation': '监测NQA TWAMP-light测试的探测结果，从测试统计的第一个结果大于等于阈值告警的上限阈值或者从大于阈值告警的下限阈值恢复到小于等于该下限阈值开始计时，若在监控时间内测试结果持续不变，打印该日志。',
                             'log_recommended_action': '无'}]


    elif module == "NQAS":

        if log_type_desc == "NQA_TWAMP_LIGHT_START_FAILURE":
            pattern_logs = [{'patterns': [
                'NQA TWAMP Light test session %{NUMBER:testSessionId:int}: Failed to start the test session. Please check the parameters.'],
                             'log_explanation': '启动TWAMP-light Responder端的测试会话失败，提示用户检查配置参数',
                             'log_recommended_action': '配置TWAMP-light Responder端测试会话的反射参数时，test-session命令TWAMP-light Responder端缺少参数必配项，根据当前网络环境判断参数的必配项，并检查参数配置并重新将参数配置完整'}]


    elif module == "NSS":

        if log_type_desc == "NSS_ENABLE_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply the command session-based netstream enable to the driver. Reason: %{DATA:param0}.'],
                             'log_explanation': 'session-based netstream enable命令下发驱动失败',
                             'log_recommended_action': '1.      检查FPGA子卡是否在位，并重新下发命令\n2.      检查设备上是否配置了NetStream或sFlow（基于会话的NetStream、NetStream和sFlow三者间存在冲突，同一时间设备仅支持运行其中一种功能）'}]

        elif log_type_desc == "NSS_SESSION_TIMEOUT_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply the command session-based netstream session-timeout to the driver. Reason: %{DATA:param0}.'],
                             'log_explanation': 'session-based netstream session-timeout命令下发驱动失败',
                             'log_recommended_action': '检查FPGA子卡是否在位，并重新下发命令'}]


    elif module == "NTP":

        if log_type_desc == "NTP_CLOCK_CHANGE":
            pattern_logs = [{'patterns': [
                "System clock changed from %{DATA:param0} to %{DATA:param1}, the NTP server's IP address is %{DATA:param2}."],
                             'log_explanation': 'NTP客户端的时间已经和NTP服务器同步', 'log_recommended_action': '无'}]

        elif log_type_desc == "NTP_LEAP_CHANGE":
            pattern_logs = [{'patterns': [
                'System Leap Indicator changed from %{NUMBER:originalLeapIndicator:int} to %{NUMBER:currentLeapIndicator:int} after clock update.'],
                             'log_explanation': '·          NTP闰秒标识是一个二位码，预报当天最近的分钟里要被插入的闰秒秒数\n·          比特值在闰秒秒数插入当天23:59前或次日00:00后设置。因此秒数会比插入当天的时间提前或推后1秒\n·          系统的闰秒标识会发生变化。例如，NTP状态会从未同步状态变为已同步状态',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "NTP_SOURCE_CHANGE":
            pattern_logs = [{'patterns': [
                "NTP server's IP address changed from %{DATA:ipAddressOriginalTimeSource} to %{DATA:ipAddressNewTimeSource}."],
                             'log_explanation': '系统改变了时钟源', 'log_recommended_action': '无'}]

        elif log_type_desc == "NTP_SOURCE_LOST":
            pattern_logs = [{'patterns': ['Lost synchronization with NTP server with IP address %{DATA:ipAddress}.'],
                             'log_explanation': 'NTP交互中的时钟源处于未同步状态或不可达',
                             'log_recommended_action': '1.      检查NTP服务器及网络连接\n2.      若NTP服务器故障，请在客户端配置新的服务器作为时钟源'}]

        elif log_type_desc == "NTP_STRATUM_CHANGE":
            pattern_logs = [{'patterns': [
                'System stratum changed from %{NUMBER:originalStratum:int} to %{NUMBER:currentStratum:int} after clock update.'],
                             'log_explanation': '系统的层数已发生变化', 'log_recommended_action': '无'}]


    elif module == "OAP":

        if log_type_desc == "OAP_CLIENT_DEREG":
            pattern_logs = [
                {'patterns': ['OAP client %{NUMBER:clientId:int} on interface %{DATA:interfaceTypeName} deregistered.'],
                 'log_explanation': '接口上承载的OAP client已取消注册', 'log_recommended_action': '检查OAP client的登录信息'}]

        elif log_type_desc == "OAP_CLIENT_TIMEOUT":
            pattern_logs = [
                {'patterns': ['OAP client %{NUMBER:clientId:int} on interface %{DATA:interfaceTypeName} timed out.'],
                 'log_explanation': '接口上承载的OAP client超时', 'log_recommended_action': '检查故障链路'}]


    elif module == "OBJP":

        if log_type_desc == "OBJP_ACCELERATE_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to accelerate %{DATA:objectPolicyVersion} object-policy %{DATA:objectPolicyName}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统加速对象策略失败',
                             'log_recommended_action': '删除一些规则或者关闭其他对象策略的加速功能，释放硬件资源'}]

        elif log_type_desc == "OBJP_ACCELERATE_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'Failed to accelerate %{DATA:objectPolicyVersion} object-policy %{DATA:objectPolicyName}. Object-policy acceleration is not supported.'],
                             'log_explanation': '因系统不支持对象策略加速而导致对象策略加速失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "OBJP_ACCELERATE_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to accelerate %{DATA:objectPolicyVersion} object-policy %{DATA:objectPolicyName}.'],
                             'log_explanation': '因系统故障导致对象策略加速失败', 'log_recommended_action': '无'}]


    elif module == "OFP":

        if log_type_desc == "OFP_ACTIVE":
            pattern_logs = [{'patterns': ['Activate openflow instance %{NUMBER:instanceId:int}'],
                             'log_explanation': '收到激活OpenFlow实例的命令', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_ACTIVE_FAILED":
            pattern_logs = [{'patterns': ['Failed to activate instance %{NUMBER:instanceId:int}.'],
                             'log_explanation': '激活OpenFlow实例失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_CONNECT":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int}, controller %{DATA:controllerId} is %{DATA:connectionStatus}.'],
                             'log_explanation': '控制器连接状态变化', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FAIL_OPEN":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} is in fail %{DATA:connectionInterruptionMode} mode.'],
                             'log_explanation': '实例激活后无法连接控制器或者从所有控制器断开，显示连接中断模式', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FAIL_OPEN_FAILED":
            pattern_logs = [{'patterns': [
                'OpenFlow instance %{NUMBER:param0:int}: %{DATA:param1} fail-open mode configuration failed and the secure mode is restored.'],
                             'log_explanation': '由于系统资源不足等原因，OpenFlow实例的连接中断模式配置失败（相关命令为fail-open mode），将回退为缺省模式Secure',
                             'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_FLOW_ADD":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: add flow entry %{NUMBER:ruleId:int}, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookieFlowEntry}, table id %{DATA:tableId}.'],
                             'log_explanation': '收到修改流表信息（增加操作）并通过报文检查。即将添加流表项', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_ADD_ARP_FAILED":
            pattern_logs = [{'patterns': [
                'Failed to add OpenFlow ARP entry: IPAddr=%{DATA:ipAddressOpenflowArpEntry}, OutIfIndex=%{NUMBER:indexOutgoingInterfaceOpenflowArpEntry:int}, MACAddr=%{DATA:macAddressOpenflowArpEntry}.'],
                             'log_explanation': 'OpenFlow ARP表项添加失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_FLOW_ADD_DUP":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: add duplicate flow entry %{NUMBER:ruleId:int}, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookie}, table id %{DATA:tableId}.'],
                             'log_explanation': '表项重复添加', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_ADD_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to add flow entry %{NUMBER:ruleId:int},table id %{DATA:tableId},because of insufficient resources.'],
                             'log_explanation': '由于资源不足，添加流表项失败', 'log_recommended_action': '请联系技术支持'}, {'patterns': [
                'Openflow instance %{NUMBER:param0:int} controller %{DATA:param1}: failed to add flow entry %{NUMBER:param2:int}, table id %{DATA:param3}.'],
                                                                                                         'log_explanation': '添加流表项失败',
                                                                                                         'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_FLOW_ADD_ND_FAILED":
            pattern_logs = [{'patterns': [
                'Failed to add OpenFlow ND entry: IPv6Addr=%{DATA:ipv6AddressOpenflowNdEntry}, OutIfIndex=%{NUMBER:indexOutgoingInterfaceOpenflowNdEntry:int}, MACAddr=%{DATA:macAddressOpenflowNdEntry}.'],
                             'log_explanation': 'OpenFlow ND表项添加失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_FLOW_ADD_TABLE_MISS":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: add table miss flow entry, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookieFlowEntry}, table id %{DATA:tableId}.'],
                             'log_explanation': '收到修改流表信息（增加操作）并通过报文检查。即将添加miss规则', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_ADD_TABLE_MISS_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to add table miss flow entry, table id %{DATA:tableId}.'],
                             'log_explanation': '添加miss规则失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_DEL":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: delete flow entry, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookieFlowEntry}, table id %{DATA:tableId}.'],
                             'log_explanation': '收到修改流表信息（删除操作）并通过报文检查。即将删除对应的流表项', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_DEL_L2VPN_DISABLE":
            pattern_logs = [{'patterns': [
                '%{NUMBER:totalNumberDeletedFlowEntries:int} flow entries in table %{NUMBER:tableId:int} of instance %{NUMBER:instanceId:int} were deleted because L2VPN was disabled.'],
                             'log_explanation': 'L2VPN功能关闭导致多个流表项被删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_DEL_TABLE_MISS":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: delete table miss flow entry, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookieFlowEntry}, table id %{DATA:tableId}.'],
                             'log_explanation': '收到修改流表信息（删除操作）并通过报文检查。即将删除对应的miss规则', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_DEL_TABLE_MISS_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to delete table miss flow entry, table id %{DATA:tableId}.'],
                             'log_explanation': '删除miss规则失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_DEL_VSIIF_DEL":
            pattern_logs = [{'patterns': [
                '%{NUMBER:param0:int} flow entries in table %{NUMBER:param1:int} of instance %{NUMBER:param2:int} were deleted because the Vsi-interface in VSI %{DATA:param3} was deleted.'],
                             'log_explanation': '由于VSI下的VSI虚接口被删除，导致相关流表项被删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_DEL_VXLAN_DEL":
            pattern_logs = [{'patterns': [
                '%{NUMBER:totalNumberDeletedFlowEntries:int} flow entries in table %{NUMBER:tableId:int} of instance %{NUMBER:instanceId:int} were deleted because a tunnel \\(ifindex %{NUMBER:indexTunnelInterface:int}\\) in VXLAN %{NUMBER:vxlanId:int} was deleted.'],
                             'log_explanation': 'VXLAN隧道被删除导致多个流表项被删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_MOD":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: modify flow entry, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookieFlowEntry}, table id %{DATA:tableId}.'],
                             'log_explanation': '收到修改流表信息（修改操作）并通过报文检查。即将修改对应的流表项', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_MOD_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to modify flow entry, table id %{DATA:tableId}.'],
                             'log_explanation': '修改流表项失败', 'log_recommended_action': '控制器重试修改操作或直接删除流表项'}]

        elif log_type_desc == "OFP_FLOW_MOD_TABLE_MISS":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: modify table miss flow entry, xid 0x%{DATA:xid}, cookie 0x%{DATA:cookieFlowEntry}, table id %{DATA:tableId}.'],
                             'log_explanation': '收到修改流表信息（修改操作）并通过报文检查。即将修改对应的miss规则', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_MOD_TABLE_MISS_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to modify table miss flow entry, table id %{DATA:tableId}.'],
                             'log_explanation': '修改miss规则失败', 'log_recommended_action': '控制器重试修改操作或直接删除miss规则'}]

        elif log_type_desc == "OFP_FLOW_RMV_GROUP":
            pattern_logs = [{'patterns': [
                'The flow entry %{NUMBER:ruleId:int} in table %{DATA:tableId} of instance %{NUMBER:instanceId:int} was deleted with a group_mod message.'],
                             'log_explanation': 'Group删除导致的表项删除', 'log_recommended_action': '无'}, {'patterns': [
                'The flow entry %{NUMBER:ruleId:int} in table %{DATA:tableId} of instance %{NUMBER:instanceId:int} was deleted with a meter_mod message.'],
                                                                                                   'log_explanation': 'Meter删除导致的表项删除',
                                                                                                   'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_RMV_HARDTIME":
            pattern_logs = [{'patterns': [
                'The flow entry %{NUMBER:param0:int} in table %{DATA:param1} of instance %{NUMBER:param2:int} was deleted because of an hard-time expiration.'],
                             'log_explanation': 'Hard-time超时导致的表项删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_RMV_IDLETIME":
            pattern_logs = [{'patterns': [
                'The flow entry %{NUMBER:ruleId:int} in table %{DATA:tableId} of instance %{NUMBER:instanceId:int} was deleted because of an idle-time expiration.'],
                             'log_explanation': 'Idle-time超时导致的表项删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_FLOW_SMOOTH_FAILED":
            pattern_logs = [{'patterns': [
                'OpenFlow instance %{NUMBER:instanceId:int} table %{DATA:tableId}: failed to update or synchronize flow entry %{NUMBER:flowEntryId:int}.'],
                             'log_explanation': '主备倒换时，新主用主控板更新流表项失败\n设备插入新接口板时，接口板同步主控板的流表项失败\nIRF中主从设备倒换时，新主设备更新流表项失败\nIRF中加入新成员设备时，成员设备同步主设备的流表项失败',
                             'log_recommended_action': '删除下发失败的流表项'}]

        elif log_type_desc == "OFP_GROUP_ADD":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: add group %{DATA:groupId}, xid 0x%{DATA:xid}.'],
                             'log_explanation': '收到修改group表信息（增加操作）并通过报文检查。即将添加group表项', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_GROUP_ADD_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to add group %{DATA:groupId}.'],
                             'log_explanation': '添加group表项失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_GROUP_DEL":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: delete group %{DATA:groupId}, xid %{DATA:xid}.'],
                             'log_explanation': '收到修改group表信息（删除操作）并通过报文检查。即将删除对应group表项',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_GROUP_MOD":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: modify group %{DATA:groupId}, xid 0x%{DATA:xid}.'],
                             'log_explanation': '收到修改group表信息（修改操作）并通过报文检查。即将修改对应group表项',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_GROUP_MOD_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to modify group %{DATA:groupId}.'],
                             'log_explanation': '修改group表项失败', 'log_recommended_action': '控制器重试修改操作或直接删除group表项'}]

        elif log_type_desc == "OFP_GROUP_REFRESH_FAILED":
            pattern_logs = [
                {'patterns': ['Openflow instance %{DATA:instanceId}:Failed to refresh group %{DATA:groupId}.'],
                 'log_explanation': '控制器成功下发Group表项到设备后，设备因为拔出/插入接口板或删除/重新创建接口，需要刷新该Group表项中某些bucket的接口信息，但是由于硬件资源不足或设备异常，刷新Group表项失败',
                 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_GROUP_ROLLBACK_FAILED":
            pattern_logs = [
                {'patterns': ['Openflow instance %{DATA:instanceId}:Failed to roll back group %{DATA:groupId}.'],
                 'log_explanation': '控制器修改设备的Group表项失败时，设备需要将该Group表项回退到修改前状态，但是由于硬件资源不足或设备异常，回退Group表项失败',
                 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_METER_ADD":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: add meter %{DATA:meterId}, xid 0x%{DATA:xid}.'],
                             'log_explanation': '收到修改meter表信息（增加操作）并通过报文检查。即将添加meter表项', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_METER_ADD_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to add meter %{DATA:meterId}.'],
                             'log_explanation': '添加meter表项失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "OFP_METER_DEL":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: delete meter %{DATA:meterId}, xid 0x%{DATA:xid}.'],
                             'log_explanation': '收到修改meter表信息（删除操作）并通过报文检查。即将删除指定的meter表项',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_METER_MOD":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: modify meter %{DATA:meterId}, xid 0x%{DATA:xid}.'],
                             'log_explanation': '收到修改meter表信息（修改操作）并通过报文检查。即将修改指定的meter表项',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_METER_MOD_FAILED":
            pattern_logs = [{'patterns': [
                'Openflow instance %{NUMBER:instanceId:int} controller %{DATA:controllerId}: failed to modify meter %{DATA:meterId}.'],
                             'log_explanation': '修改meter表项失败', 'log_recommended_action': '控制器重试修改操作或直接删除meter表项'}]

        elif log_type_desc == "OFP_MISS_RMV_GROUP":
            pattern_logs = [{'patterns': [
                'The table-miss flow entry in table %{DATA:tableId} of instance %{NUMBER:instanceId:int} was deleted with a group_mod message.'],
                             'log_explanation': 'Group删除导致的table-miss表项删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_MISS_RMV_HARDTIME":
            pattern_logs = [{'patterns': [
                'The table-miss flow entry in table %{DATA:param0} of instance %{NUMBER:param1:int} was deleted because of an hard-time expiration.'],
                             'log_explanation': 'Hard-time超时导致的table-miss表项删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_MISS_RMV_IDLETIME":
            pattern_logs = [{'patterns': [
                'The table-miss flow entry in table %{DATA:tableId} of instance %{NUMBER:instanceId:int} was deleted because of an idle-time expiration.'],
                             'log_explanation': 'Idle-time超时导致的table-miss表项删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_MISS_RMV_METER":
            pattern_logs = [{'patterns': [
                'The table-miss flow entry in table %{DATA:tableId} of instance %{NUMBER:instanceId:int} was deleted with a meter_mod message.'],
                             'log_explanation': 'Meter删除导致的table-miss表项删除', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_TTP_GROUP_DEL_DENY":
            pattern_logs = [{'patterns': [
                'Openflow instance %{DATA:instanceId} controller %{DATA:controllerId}: Failed to delete TTP group %{DATA:ttpGroupEntryId}, XID %{DATA:xid\\(transactionId\\)}. Reason: The TTP group is used by another TTP group.'],
                             'log_explanation': '被其他TTP Group表项引用的TTP Group表项不允许被删除',
                             'log_recommended_action': '请控制器先删除引用TTP Group表项的其他TTP Group表项，再重试删除操作'}]

        elif log_type_desc == "PORT_MOD":
            pattern_logs = [{'patterns': [
                'Port modified. InstanceID =%{NUMBER:instanceId:int}, IfIndex =%{NUMBER:interfaceIndex:int}, PortDown=%{DATA:whetherSetStatusInterface}, NoRecv=%{DATA:whetherDisableInterfaceReceivingPackets}, NoFwd=%{DATA:whetherDisableInterfaceForwardingPackets}, NoPktIn=%{DATA:whetherDisableInterfaceSendingPacketsController}, Speed=%{DATA:setsSpeedInterface}, Duplex=%{DATA:setsDuplexModeInterface}.'],
                             'log_explanation': '控制器修改了OpenFlow实例中的接口', 'log_recommended_action': '无'}]

        elif log_type_desc == "OFP_RADARDETECTION":
            pattern_logs = [{'patterns': [
                'inIfIndex = %{NUMBER:indexIngressPortPacket:int}, packageId = %{NUMBER:packetIdentifier:int}, innerTTL =  %{DATA:timeToLiveValueInnerIpHeaderPacket}, outerTTL =  %{DATA:timeToLiveValueOuterIpHeaderPacket}.'],
                             'log_explanation': '收到用于雷达探测或VM仿真功能的报文', 'log_recommended_action': '无'}]


    elif module == "OPENSRC":

        if log_type_desc == "SYSLOG":
            pattern_logs = [{'patterns': [
                '(?<LOG_DATE>%{MONTH} +%{MONTHDAY}):dateMonthAbbreviationDayFormat %{TIME:timeHh} radiusd%{NUMBER:freeradiusProcessId:int}: %{DATA:processRestartEventDescription}'],
                             'log_explanation': '进程启动时，系统加载默认检查项',
                             'log_recommended_action': '请根据进程启动的详细说明选择相应的处理方式，详见表1-3'}, {'patterns': [
                "(?<LOG_DATE>%{MONTH} +%{MONTHDAY}):dateMonthAbbreviationDayFormat %{TIME:timeHh} radiusd%{NUMBER:freeradiusProcessId:int}: \\(%{NUMBER:logId:int}\\) %{DATA:authenticationResult}: [%{DATA:userName}] \\(from client %{IP:radiusClientIpAddress} port %{NUMBER:radiusClientPortNumber:int} cli %{MAC:user'sMacAddress}\\)"],
                                                                                         'log_explanation': '用户认证成功',
                                                                                         'log_recommended_action': '请根据认证结果的详细说明选择相应的处理方式，详见表1-4'},
                            {'patterns': [
                                '(?<LOG_DATE>%{MONTH} +%{MONTHDAY}):dateMonthAbbreviationDayFormat %{TIME:timeHh} radiusd%{NUMBER:freeradiusProcessId:int}: \\(%{NUMBER:logId:int}\\) Login incorrect \\(No Auth-Type found: rejecting the user via Post-Auth-Type = Reject\\): [%{DATA:userName}] \\(from client %{IP:radiusClientIpAddress} port %{NUMBER:radiusClientPortNumber:int}\\)'],
                             'log_explanation': '不支持Login类型的用户认证', 'log_recommended_action': '不需要处理'}, {'patterns': [
                    '(?<LOG_DATE>%{MONTH} +%{MONTHDAY}):dateMonthAbbreviationDayFormat %{TIME:timeHh} radiusd%{NUMBER:freeradiusProcessId:int}: Ignoring request to auth address * port 1812 bound to server default from unknown client %{IP:radiusClientIpAddress} port %{NUMBER:radiusClientPortNumber:int} proto udp'],
                                                                                                        'log_explanation': '未知的RADIUS客户端IP地址和端口号，不处理认证请求报文',
                                                                                                        'log_recommended_action': '·          若是非法客户端，则不需要处理\n·          若是新增客户端，则通过radius-server client命令新增对应的RADIUS客户端配置'}]


    elif module == "OPTMOD":

        if log_type_desc == "BIAS_HIGH":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Bias current is high.'], 'log_explanation': '光模块的偏置电流超过上限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看当前偏置电流值是否已经超过高告警门限\n2.      display transceive alarm interface命令查看当前是否确实有偏置电流值高的告警\n3.      如果确实超过门限了，模块有问题，更换模块'}]

        elif log_type_desc == "BIAS_LOW":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Bias current is low.'], 'log_explanation': '光模块的偏置电流低于下限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看当前偏置电流值是否已经超过低告警门限\n2.      display transceive alarm interface命令查看当前是否确实有偏置电流高的告警\n3.      如果低于低告警门限，模块有问题，更换模块'}]

        elif log_type_desc == "BIAS_NORMAL":
            pattern_logs = [{'patterns': ['%{DATA:interfaceTypeNumber}: Bias current is normal.'],
                             'log_explanation': '光模块的偏置电流恢复至正常范围', 'log_recommended_action': '无'}]

        elif log_type_desc == "CFG_ERR":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Transceiver type and port configuration mismatched.'],
                 'log_explanation': '光模块类型与端口配置不匹配', 'log_recommended_action': '检查端口当前配置与光模块类型，如果确实不匹配，则更换匹配模块，或更新配置'}]

        elif log_type_desc == "CHKSUM_ERR":
            pattern_logs = [{'patterns': ['%{DATA:interfaceTypeNumber}: Transceiver information checksum error.'],
                             'log_explanation': '光模块寄存器信息校验失败', 'log_recommended_action': '更换光模块，或联系工程师解决'}]

        elif log_type_desc == "FIBER_SFPMODULE_INVALID":
            pattern_logs = [{'patterns': [
                '%{DATA:interfaceTypeNumber}: This transceiver module is not compatible with the interface card. HP does not guarantee the correct operation of the transceiver module. The transceiver module will be invalidated in %{NUMBER:numberDaysTransceiverModuleInvalid:int} days. Please replace it with a compatible one as soon as possible.'],
                             'log_explanation': '光模块与接口卡不匹配', 'log_recommended_action': '更换光模块'}]

        elif log_type_desc == "FIBER_SFPMODULE_NOWINVALID":
            pattern_logs = [{'patterns': [
                '%{DATA:param0}: This is not a supported transceiver for this platform.  HP does not guarantee the normal operation or maintenance of unsupported transceivers.  Please review the platform datasheet on the HP web site or contact your HP sales rep for a list of supported transceivers.'],
                             'log_explanation': '不支持该光模块', 'log_recommended_action': '更换光模块'}]

        elif log_type_desc == "IO_ERR":
            pattern_logs = [{'patterns': ['%{DATA:interfaceTypeNumber}: The transceiver information I/O failed.'],
                             'log_explanation': '设备读取光模块寄存器信息失败',
                             'log_recommended_action': '执行display transceive diagnosis interface或者display transceive alarm interface命令，如果都显示fail，则表示光模块故障，请更换'}]

        elif log_type_desc == "TX_ALM_OFF":
            pattern_logs = [{'patterns': ['%{DATA:interfaceTypeNumber}: %{DATA:txFaultType} was removed.'],
                             'log_explanation': '光模块TX故障被清除', 'log_recommended_action': '无'}]

        elif log_type_desc == "RX_ALM_ON":
            pattern_logs = [{'patterns': ['%{DATA:interfaceTypeNumber}: %{DATA:rxFaultType} was detected.'],
                             'log_explanation': '检测到光模块RX故障',
                             'log_recommended_action': '使用display transceive alarm interface命令可查看到这个故障，确认是模块问题，更换模块'}]

        elif log_type_desc == "MODULE_IN":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: The transceiver is %{DATA:typeTransceiverModule}.'],
                 'log_explanation': '光模块类型。当一光模块插入某端口时，设备生成此日志信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "MODULE_OUT":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Transceiver absent.'], 'log_explanation': '光模块被拔出',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "PHONY_MODULE":
            pattern_logs = [{'patterns': [
                '%{DATA:interfaceTypeNumber}: This transceiver is not sold by H3C. H3C does not guarantee the correct operation of the module or assume maintenance responsibility.'],
                             'log_explanation': '光模块非H3C生产', 'log_recommended_action': '更换光模块'}]

        elif log_type_desc == "RX_POW_HIGH":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: RX power is high.'], 'log_explanation': '光模块RX功率超过上限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看功率是否已经超过高告警门限\n2.      display transceive alarm interface命令查看当前是否确实有功率高的告警\n3.      如果确实超过门限了，模块有问题，更换模块'}]

        elif log_type_desc == "RX_POW_LOW":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: RX power is low.'], 'log_explanation': '光模块RX功率低于下限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看功率是否已经低于低告警门限\n2.      display transceive alarm interface命令查看当前是否确实有功率低告警\n3.      如果确实低于门限了，模块有问题，更换模块'}]

        elif log_type_desc == "RX_POW_NORMAL":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: RX power is normal.'], 'log_explanation': '光模块RX功率恢复至正常范围',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "TEMP_HIGH":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Temperature is high.'], 'log_explanation': '光模块温度超过上限',
                 'log_recommended_action': '检查设备风扇是否工作正常，安装风扇或更换故障风扇\n检查环境温度，如果温度确实过高就调节温度\n如果设备风扇正常，且环境温度正常，则模块故障，更换模块'}]

        elif log_type_desc == "TEMP_LOW":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Temperature is low.'], 'log_explanation': '光模块温度低于下限',
                 'log_recommended_action': '检查环境温度，如果温度确实过低高就调节温度，如果环境温度正常，就是模块故障，更换模块'}]

        elif log_type_desc == "TEMP_NORMAL":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Temperature is normal.'], 'log_explanation': '光模块温度恢复至正常范围',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "TX_ALM_ON":
            pattern_logs = [{'patterns': ['%{DATA:interfaceTypeNumber}: %{DATA:txFaultType} was  detected.'],
                             'log_explanation': '检测到光模块TX故障',
                             'log_recommended_action': '使用display transceive alarm interface命令可查看到这个故障，确认是模块问题，更换模块'}]

        elif log_type_desc == "TX_POW_HIGH":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: TX power is high.'], 'log_explanation': '光模块TX功率超过上限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看功率是否已经超过高告警门限\n2.      display transceive alarm interface命令查看当前是否确实有功率高告警\n3.      如果确实超过门限了，模块有问题，更换模块'}]

        elif log_type_desc == "TX_POW_LOW":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: TX power is low.'], 'log_explanation': '光模块TX功率低于下限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看功率是否已经低于低告警门限\n2.      display transceive alarm interface命令查看当前是否确实有功率低告警\n3.      如果确实低于门限了，模块有问题，更换模块'}]

        elif log_type_desc == "TX_POW_NORMAL":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: TX power is normal.'], 'log_explanation': '光模块TX功率恢复至正常范围',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "TYPE_ERR":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: The transceiver type is not supported by port hardware.'],
                 'log_explanation': '端口硬件不支持光模块类型', 'log_recommended_action': '更换光模块'}]

        elif log_type_desc == "VOLT_HIGH":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Voltage is high.'], 'log_explanation': '光模块电压超过上限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看电压是否已经超过高告警门限\n2.      display transceive alarm interface命令查看当前是否确实有电压高告警\n3.      如果确实超过门限了，模块有问题，更换模块'}]

        elif log_type_desc == "VOLT_LOW":
            pattern_logs = [
                {'patterns': ['%{DATA:interfaceTypeNumber}: Voltage is low.'], 'log_explanation': '光模块电压低于下限',
                 'log_recommended_action': '1.      display transceive diagnosis interface命令查看电压是否已经超过低告警门限\n2.      display transceive alarm interface命令查看当前是否确实有电压低告警\n3.      如果确实超过门限了，模块有问题，更换模块'}]

        elif log_type_desc == "VOLT_NORMAL":
            pattern_logs = [{'patterns': ['%{DATA:param0}: Voltage is normal.'], 'log_explanation': '光模块电压恢复至正常范围',
                             'log_recommended_action': '无'}]


    elif module == "OSPF":

        if log_type_desc == "OSPF_DUP_RTRID_NBR":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Duplicate router ID %{DATA:routerId} on interface %{DATA:interfaceName}, sourced from IP address %{IP:ipAddress}.'],
                             'log_explanation': '检测到两台直连设备配置了相同的路由器ID',
                             'log_recommended_action': '修改其中一台设备的路由器ID，并使用reset ospf process命令使新的路由器ID生效'}]

        elif log_type_desc == "OSPF_IP_CONFLICT_INTRA":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Received newer self-originated network-LSAs. Possible conflict of IP address %{IP:ipAddress} in area %{DATA:ospfAreaId} on interface %{DATA:interfaceName}.'],
                             'log_explanation': '同一OSPF区域内两台设备的接口上可能配置了相同的主IP地址，其中至少一台设备是DR',
                             'log_recommended_action': '在确保同一OSPF区域内不存在Router ID冲突的情况下，修改IP地址配置'}]

        elif log_type_desc == "OSPF_LAST_NBR_DOWN":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Last neighbor down event: Router ID: %{DATA:routerId} Local address: %{DATA:localIpAddress} Remote address: %{DATA:neighborIpAddress} Reason: %{DATA:reason}'],
                             'log_explanation': '最近一次OSPF邻居down事件',
                             'log_recommended_action': '检查OSPF邻居down事件的原因，根据具体原因进行处理：\n·          如果是配置相关命令导致邻居down，如接口参数变化等，请检查配置是否正确\n·          如果是超时邻居down，检查网络状况或者配置的超时时间是否合理\n·          如果是BFD检测导致的邻居down ，检查网络状况或者BFD检测时间配置是否合理\n·          如果是接口状态变化导致的邻居down，检查网络连接情况'}]

        elif log_type_desc == "OSPF_MEM_ALERT":
            pattern_logs = [{'patterns': ['OSPF Process received system memory alert %{DATA:typeMemoryAlarm} event.'],
                             'log_explanation': 'OSPF模块收到内存告警信息',
                             'log_recommended_action': '当超过各级内存门限时，检查系统内存，对占用内存较多的模块进行调整，尽量释放可用内存'}]

        elif log_type_desc == "OSPF_NBR_CHG":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Neighbor %{DATA:neighborRouterId} \\(%{DATA:interfaceName}\\) changed from %{DATA:oldAdjacencyState} to %{DATA:newAdjacencyState}.'],
                             'log_explanation': '接口OSPF邻接状态改变',
                             'log_recommended_action': '当某接口与邻居的状态发生改变时发送该日志，请检查OSPF配置正确性和网络连通性'}]

        elif log_type_desc == "OSPF_NBR_CHG_REASON":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Area %{DATA:areaId} Router %{DATA:routerId}\\(%{DATA:interfaceName}\\) CPU usage: %{DATA:cpuUtilization}, VPN name: %{DATA:vpnName}, IfMTU: %{NUMBER:interfaceMtu:int}, Neighbor address: %{DATA:neighborIpAddress}, NbrID %{DATA:neighborRouterId} changed from %{DATA:oldNeighborState} to %{DATA:newNeighborStateReason} at %{DATA:neighborStateChangeTime}.\nLast 4 hello packets received at:\n%{DATA:timeLastFourHelloPacketsReceivedNeighborStateChange}\nLast 4 hello packets sent at:\n%{DATA:timeLastFourHelloPacketsSentNeighborStateChange}'],
                             'log_explanation': '接口OSPF邻居状态改变',
                             'log_recommended_action': '当某接口与邻居的状态发生回退时发送该日志，请检查OSPF配置正确性和网络连通性'}]

        elif log_type_desc == "OSPF_RT_LMT":
            pattern_logs = [{'patterns': ['OSPF %{NUMBER:ospfProcessId:int} route limit reached.'],
                             'log_explanation': 'OSPF进程的路由数达到了上限值', 'log_recommended_action': '检查是否受到攻击或者减少网络路由数'}]

        elif log_type_desc == "OSPF_RTRID_CHG":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} New router ID elected, please restart OSPF if you want to make the new router ID take effect.'],
                             'log_explanation': '用户更改了router ID或者是使用的接口IP发生变化而改变了OSPF路由器ID。需要手动重启OSPF使新的路由器ID生效',
                             'log_recommended_action': '使用reset ospf process命令使新的路由器ID生效'}]

        elif log_type_desc == "OSPF_RTRID_CONFILICT_INTER":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Received newer self-originated ase-LSAs. Possible conflict of router ID %{DATA:routerId}.'],
                             'log_explanation': '同一OSPF域内非直连的两台设备可能配置了相同的路由器ID，其中一台设备为ASBR',
                             'log_recommended_action': '修改其中一台设备的路由器ID，并使用reset ospf process命令使新的路由器ID生效'}]

        elif log_type_desc == "OSPF_RTRID_CONFLICT_INTRA":
            pattern_logs = [{'patterns': [
                'OSPF %{NUMBER:ospfProcessId:int} Received newer self-originated router-LSAs. Possible conflict of router ID %{DATA:routerId} in area %{DATA:ospfAreaId}.'],
                             'log_explanation': '同一OSPF区域内非直连的两台设备可能配置了相同的路由器ID',
                             'log_recommended_action': '修改其中一台设备的路由器ID，并使用reset ospf process命令使新的路由器ID生效'}]

        elif log_type_desc == "OSPF_VLINKID_CHG":
            pattern_logs = [
                {'patterns': ['OSPF %{NUMBER:ospfProcessId:int} Router ID changed, reconfigure Vlink on peer'],
                 'log_explanation': '新的OSPF路由器ID生效。需要根据新的路由器ID检查并修改对端路由器的虚连接配置',
                 'log_recommended_action': '根据新的路由器ID检查并修改对端路由器的虚连接配置'}]


    elif module == "OSPFV3":

        if log_type_desc == "OSPFV3_LAST_NBR_DOWN":
            pattern_logs = [{'patterns': [
                'OSPFv3 %{NUMBER:ospfv3ProcessId:int} Last neighbor down event: Router ID: %{DATA:routerId}  Local interface ID: %{NUMBER:localInterfaceId:int}  Remote interface ID: %{NUMBER:remoteInterfaceId:int}  Reason: %{DATA:reason}.'],
                             'log_explanation': '最近一次OSPFv3邻居down事件',
                             'log_recommended_action': '检查OSPFV3邻居down事件的原因，根据具体原因进行处理：\n·          如果是配置相关命令导致邻居down，如接口参数变化等，请检查配置是否正确\n·          如果是超时邻居down，检查网络状况或者配置的超时时间是否合理\n·          如果是BFD检测导致的邻居down ，检查网络状况或者BFD检测时间配置是否合理\n·          如果是接口状态变化导致的邻居down，检查网络连接情况'}]

        elif log_type_desc == "OSPFV3_MEM_ALERT":
            pattern_logs = [{'patterns': ['OSPFV3 Process received system memory alert %{DATA:typeMemoryAlarm} event.'],
                             'log_explanation': 'OSPFv3模块收到内存告警信息',
                             'log_recommended_action': '当超过各级内存门限时，检查系统内存占用情况，对占用内存较多的模块进行调整，尽量释放可用内存'}]

        elif log_type_desc == "OSPFV3_NBR_CHG":
            pattern_logs = [{'patterns': [
                'OSPFv3 %{NUMBER:processId:int} Neighbor %{DATA:neighborRouterId} \\(%{DATA:interfaceName}\\) received %{DATA:neighborEvent} and its state from %{DATA:oldAdjacencyState} to %{DATA:newAdjacencyState}.'],
                             'log_explanation': '接口OSPFv3邻接状态改变',
                             'log_recommended_action': '当某接口与邻居邻接状态从Full变为其他状态时，检查OSPFv3配置正确性和网络连通性'}]

        elif log_type_desc == "OSPFV3_RT_LMT":
            pattern_logs = [{'patterns': ['OSPFv3 %{NUMBER:processId:int} route limit reached.'],
                             'log_explanation': 'OSPFv3进程的路由数达到了上限值', 'log_recommended_action': '检查是否受到攻击或者减少网络路由数'}]


    elif module == "PBB":

        if log_type_desc == "PBB_JOINAGG_WARNING":
            pattern_logs = [{'patterns': [
                'Because the aggregate interface %{DATA:aggregationGroupName} has been configured with PBB, assigning the interface %{DATA:interfaceName} that does not support PBB to the aggregation group will cause incorrect processing.'],
                             'log_explanation': '将不支持PBB的接口加入已经配置了PBB的聚合组会引发处理错误，配置为PBB实例上行口的聚合组的成员端口都需支持PBB',
                             'log_recommended_action': '将该接口从聚合组中删除'}]


    elif module == "PBR":

        if log_type_desc == "PBR_HARDWARE_ERROR":
            pattern_logs = [
                {'patterns': ['Failed to update policy %{DATA:policyName} due to %{DATA:hardwareErrorReasons}.'],
                 'log_explanation': '更新单播策略路由配置失败', 'log_recommended_action': '根据失败原因修改策略中的配置'}]


    elif module == "PEX":

        if log_type_desc == "PEX_ASSOCIATEID_MISMATCHING":
            pattern_logs = [{'patterns': [
                'The associated ID of PEX port %{NUMBER:pexPortId:int} is %{NUMBER:virtualSlotChassisNumberConfiguredParentFabricPex:int} on the parent fabric, but the PEX connected to the port has obtained ID %{NUMBER:virtualSlotChassisNumberPexObtained:int}.'],
                             'log_explanation': '用户配置的associate ID 与实际连接的PEX设备associate ID不一致',
                             'log_recommended_action': '请检查组网连接'}]

        elif log_type_desc == "PEX_CONFIG_ERROR":
            pattern_logs = [{'patterns': [
                'PEX port %{NUMBER:pexPortId:int} discarded a REGISTER request received from %{DATA:pexModel} through interface %{DATA:namePexPhysicalInterface}. Reason: The PEX was not assigned an ID, or the PEX was assigned an ID equal to or greater than the maximum value \\(%{NUMBER:maximumVirtualSlotChassisNumberPexModel:int}\\).'],
                             'log_explanation': 'PEX设备启动前必须通过associate命令配置虚拟槽位号或虚拟框号\nPEX不同型号的产品允许分配的虚拟槽位号/虚拟框号有最大值限制\nXX型号的连接到XX端口的PEX没有配置虚拟槽位号/虚拟框号或者配置的虚拟槽位号/虚拟框号超过了产品允许的最大范围',
                             'log_recommended_action': '通过associate命令将分配给PEX的槽号修改到正确的虚拟槽位号/虚拟框号范围内'}]

        elif log_type_desc == "PEX_CONNECTION_ERROR":
            pattern_logs = [{'patterns': [
                'PEX port %{NUMBER:pexPortId:int} discarded a REGISTER request received from %{DATA:pexModel} through interface %{DATA:namePexPhysicalInterface}. Reason: Another PEX has been registered on the PEX port.'],
                             'log_explanation': '每个PEX端口只允许加入一个PEX设备，如果有一个PEX已经启动，其他的PEX连接到该端口上属于配置错误，丢弃请求',
                             'log_recommended_action': '检查连线是否错误，请确认同一个PEX端口下只连接了一个PEX设备'}]

        elif log_type_desc == "PEX_FORBID_STACK":
            pattern_logs = [{'patterns': [
                "Can't connect PEXs %{NUMBER:virtualSlotChassisNumberPex:int} and %{NUMBER:virtualSlotChassisNumberPex:int}: The PEX ports to which the PEXs belong are in different PEX port groups."],
                             'log_explanation': '属于不同PEX端口组的PEX设备连接在一起', 'log_recommended_action': '请检查组网连接'}]

        elif log_type_desc == "PEX_LINK_BLOCK":
            pattern_logs = [{'patterns': [
                'Status of %{DATA:namePexPhysicalInterface} changed from %{DATA:dataLinkStatusInterface} to blocked.'],
                             'log_explanation': '处于blocked状态的链路可以转发协议包，但是不能转发数据包。Blocked是一种介于down与forwarding之间的过渡状态\n下面的事件可以触发PEX链路状态进入blocked状态：\n·          物理连接错误，即同一PEX设备上的PEX物理接口连接到了父设备上不同PEX端口下绑定的PEX物理接口或者父设备上同一PEX端口下绑定的PEX物理接口连接到了不同的PEX设备\n·          被设备强制限制成Blocked状态。在PEX设备启动阶段，PEX设备会将未被用于加载启动软件包的、物理状态为UP的PEX物理端口状态设置为Blocked\n·          接口的物理状态为UP，但是父设备和PEX设备的PEX连接中断',
                             'log_recommended_action': '从down到blocked，说明接口up了，属于正常状态。但是如果长期停在blocked状态，请确认连线是否正确或者线路是否正常\n从forwarding到blocked，并且长期停在blocked，请检查是否存在IRF分裂，导致PEX存在两个IRF中'}]

        elif log_type_desc == "PEX_LINK_DOWN":
            pattern_logs = [{'patterns': [
                'Status of %{DATA:namePexPhysicalInterface} changed from %{DATA:dataLinkStatusInterface} to down.'],
                             'log_explanation': '处于down状态的链路无法转发任何报文\n许多事件，例如：物理链路故障、管理员执行shutdown命令、系统重启等等，都可以使链路进入down状态',
                             'log_recommended_action': '请确认是否有管理员输入shutdown命令或者系统重启操作导致，如果是以上操作导致，则属于正常状态。如果不是，请检查物理接口的连线是否进行过插拔操作或松动'}]

        elif log_type_desc == "PEX_LINK_FORWARD":
            pattern_logs = [{'patterns': [
                'Status of %{DATA:namePexPhysicalInterface} changed from %{DATA:dataLinkStatusInterface} to forwarding.'],
                             'log_explanation': '·          链路进入forwarding状态，可以开始转发数据报文\n·          下面的事件可以触发PEX链路进入forwarding状态：\n¡  链路进入blocked状态后，重新检测成功\n¡  PEX完成软件加载，使PEX端口状态变成forwarding',
                             'log_recommended_action': '正常状态，无需任何处理'}]

        elif log_type_desc == "PEX_REG_JOININ":
            pattern_logs = [{'patterns': [
                'PEX \\(%{DATA:virtualSlotChassisNumberPex}\\) registered successfully on PEX port %{NUMBER:pexPortId:int}.'],
                             'log_explanation': 'PEX端口完成注册，可以开始管理及配置PEX设备。在父设备上可以将PEX设备视为一块接口板进行操作',
                             'log_recommended_action': '正常事件，无需任何处理'}]

        elif log_type_desc == "PEX_REG_LEAVE":
            pattern_logs = [{'patterns': [
                'PEX \\(%{DATA:virtualSlotChassisNumberPex}\\) unregistered on PEX port %{NUMBER:pexPortId:int}.'],
                             'log_explanation': 'PEX端口取消注册，此后从父设备上无法操作PEX设备\n下面的事件可以导致PEX端口取消注册：\n·          PEX设备在30分钟内启动失败\n·          PEX端口内的所有物理接口down。例如将所有和父设备连接的接口都shutdown或者将物理连接全部断开\n·          PEX端口内的所有物理端口的链路检测均失败\n·          PEX设备重启',
                             'log_recommended_action': '1.      如果是PEX设备重启或者用户将PEX和父设备之间的相连的所有端口都手工关闭了导致PEX设备取消注册，属于正常事件，无需任何处理\n2.      否则，请使用命令行display device查看PEX的设备的虚拟槽位号/虚拟框号是否存在，State是否正常，以及display pex-port检查PEX端口配置是否存在，或者PEX物理端口状态是否全部为down或者全部blocked\n3.      使用命令行display interface检查PEX端口内的所有物理接口对应的Current state字段是否为down'}]

        elif log_type_desc == "PEX_REG_REQUEST":
            pattern_logs = [{'patterns': [
                'Received a REGISTER request on PEX port %{NUMBER:pexPortId:int} from PEX \\(%{DATA:virtualSlotChassisNumberPex}\\).'],
                             'log_explanation': 'PEX相关配置已经成功，PEX设备和父设备连线正确，PEX设备启动时候，PEX端口收到注册请求后准备启动加载版本',
                             'log_recommended_action': '正常事件，无需任何处理'}]

        elif log_type_desc == "PEX_STACKCONNECTION_ERROR":
            pattern_logs = [{'patterns': ['A device was connected to a PEX that already had two neighboring devices.'],
                             'log_explanation': '系统中存在连接错误，有一条链路连接到了一个PEX，这个PEX已经存在两个邻居设备',
                             'log_recommended_action': '请检查组网连接'}]

        elif log_type_desc == "PEX_AUTOCONFIG_BAGG_ASSIGNMEMBER":
            pattern_logs = [
                {'patterns': ['%{DATA:physicalInterfaceName} was assigned to %{DATA:layer2AggregateInterfaceName}.'],
                 'log_explanation': '父设备运行IRF3.1系统自动配置功能时，自动将连接PEX的物理接口添加到作为级联接口的聚合组中',
                 'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_AUTOCONFIG_BAGG_CREATE":
            pattern_logs = [
                {'patterns': ['%{DATA:layer2AggregateInterfaceName} was created by the PEX auto-config feature.'],
                 'log_explanation': '父设备运行IRF3.1系统自动配置功能时，自动创建二层聚合接口用来作级联接口', 'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_AUTOCONFIG_BAGG_NORESOURCE":
            pattern_logs = [{'patterns': ['Not enough resources to create a Layer 2 aggregate interface.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，没有空闲资源创建二层聚合接口',
                             'log_recommended_action': '删除设备上不需要使用的聚合接口，释放资源'}]

        elif log_type_desc == "PEX_AUTOCONFIG_BAGG_REMOVEMEMBER":
            pattern_logs = [
                {'patterns': ['%{DATA:physicalInterfaceName} was removed from %{DATA:layer2AggregateInterfaceName}.'],
                 'log_explanation': '父设备运行IRF3.1系统自动配置功能时，会自动将连接PEX的物理接口添加到作为级联接口的聚合组中。添加端口时，如果检查到该物理接口已经被添加到其他级联接口的聚合组中，则先将该物理接口从其他级联接口的聚合组中删除',
                 'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_AUTOCONFIG_CAPABILITY_ENABLE":
            pattern_logs = [{'patterns': [
                'PEX connection capability was enabled on %{DATA:layer2AggregateInterfaceName} and the interface was assigned to PEX group %{NUMBER:pexGroupNumber:int}.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，自动开启连接PEX的二层聚合接口的PEX连接能力，并将该接口加入PEX组中',
                             'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_AUTOCONFIG_CASCADELIMIT":
            pattern_logs = [{'patterns': [
                'Failed to assign cascade port %{DATA:layer2AggregateInterfaceName} to PEX group %{NUMBER:pexGroupNumber:int}. Reason: Maximum number of cascade ports already reached in the PEX group.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，检测到PEX组中级联接口的数目已达到上限，无法再将聚合接口加入该PEX组中',
                             'log_recommended_action': '删除该组中空闲的级联接口，释放资源'}]

        elif log_type_desc == "PEX_AUTOCONFIG_CONNECTION_ERROR":
            pattern_logs = [{'patterns': ['A PEX connected to more than one upper-tier PEXs.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，检测到PEX和两台或两台以上上级PEX之间存在物理连接',
                             'log_recommended_action': 'PEX上行链路只能连接到同一台上级PEX，否则可能导致PEX无法上线或上线后功能运行异常。请检查并修改组网连接'}]

        elif log_type_desc == "PEX_AUTOCONFIG_DIFFGROUPNUMBER":
            pattern_logs = [{'patterns': [
                '%{DATA:param0} failed to join in PEX group %{NUMBER:param1:int}. Reason: Its upper-tier PEX was in PEX group %{NUMBER:param2:int}. Please make sure they are in the same PEX group.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能，开启PEX二层聚合接口连接PEX的能力并将接口加入PEX组时，所指定的PEX组编号与上级PEX所在PEX组编号不同。',
                             'log_recommended_action': '下级PEX只能与上级PEX加入同一PEX组，请修改配置'}]

        elif log_type_desc == "PEX_AUTOCONFIG_DYNAMICBAGG_STP":
            pattern_logs = [{'patterns': [
                '%{DATA:layer2AggregateInterfaceName} was automatically set to dynamic aggregation mode and configured as an STP edge port.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，将级联接口自动配置为动态聚合模式并且配置为STP边缘端口。',
                             'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_AUTOCONFIG_GROUP_CREATE":
            pattern_logs = [{'patterns': ['PEX group %{NUMBER:pexGroupNumber:int} was created.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，自动创建PEX组', 'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_AUTOCONFIG_NONUMBERRESOURCE":
            pattern_logs = [
                {'patterns': ['No virtual slot numbers are available.', 'No virtual chassis numbers are available.'],
                 'log_explanation': '父设备运行IRF3.1系统自动配置功能时，没有虚拟槽位号/虚拟框号资源用来分配',
                 'log_recommended_action': '删除空闲级联接口或在空闲级联接口上取消分配虚拟槽位号/虚拟框号的配置，释放资源'}]

        elif log_type_desc == "PEX_AUTOCONFIG_NOT_CASCADEPORT":
            pattern_logs = [{'patterns': [
                '%{DATA:physicalInterfaceName} was already assigned to %{DATA:layer2AggregateInterfaceName}, which is an aggregate interface not enabled with PEX connection capability. Please remove %{DATA:physicalInterfaceName} from %{DATA:layer2AggregateInterfaceName} or use another physical interface to connect the PEX.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，检测到连接PEX的物理接口已经加入到聚合组中，但对应聚合接口没有开启连接PEX的能力',
                             'log_recommended_action': '将物理接口从聚合组中退出或更换其他物理接口'}]

        elif log_type_desc == "PEX_AUTOCONFIG_NUMBER_ASSIGN":
            pattern_logs = [{'patterns': [
                'Virtual slot number %{NUMBER:virtualSlotNumber:int} was assigned on %{DATA:layer2AggregateInterfaceName}.',
                'Virtual chassis number %{NUMBER:virtualChassisNumber:int} was assigned on %{DATA:layer2AggregateInterfaceName}.'],
                             'log_explanation': '父设备运行IRF3.1系统自动配置功能时，在连接PEX的二层聚合接口上，自动为PEX分配虚拟槽位号/虚拟框号',
                             'log_recommended_action': '不需要处理'}]

        elif log_type_desc == "PEX_LLDP_DISCOVER":
            pattern_logs = [
                {'patterns': ['Discover peer device on interface %{DATA:param0}: MAC=STRING, priority=UINT32.'],
                 'log_explanation': '父设备或PEX设备通过LLDP协议发现对端', 'log_recommended_action': '正常状态，无需任何处理'}]

        elif log_type_desc == "PEX_MEMBERID_EXCEED":
            pattern_logs = [{'patterns': [
                'To use the IRF fabric connected to interface %{DATA:interfaceName} as a PEX, the IRF member ID must be in the range of 1 to 4.'],
                             'log_explanation': '设备作为PEX加入IRF3.1系统时，PEX设备的IRF成员编号必须在1~4范围以内',
                             'log_recommended_action': '请检查PEX设备的IRF成员编号是否在1～4范围之内。如果不是，用户可登录PEX设备，用irf member renumber命令修改PEX设备的成员编号'}]

        elif log_type_desc == "PEX_PECSP_OPEN_RCVD":
            pattern_logs = [{'patterns': ['Received a CSP Open message on interface %{DATA:interfaceName}.'],
                             'log_explanation': '接口收到PE CSP协议的OPEN报文，表示对端请求建立连接。如果双方均能在发送请求后60秒内接收到对端回复的OPEN报文，则父设备和PEX之间的连接建立成功',
                             'log_recommended_action': '正常状态，无需任何处理'}]

        elif log_type_desc == "PEX_PECSP_OPEN_SEND":
            pattern_logs = [{'patterns': ['Sent a CSP Open message on interface %{DATA:interfaceName}.'],
                             'log_explanation': '父设备级联口或PEX设备上行口发送PE CSP协议的OPEN报文，表示请求与对方建立连接。如果双方均能在发送请求后60秒内接收到对端回复的OPEN报文，则父设备和PEX之间的连接建立成功',
                             'log_recommended_action': '正常状态，无需任何处理'}]

        elif log_type_desc == "PEX_PECSP_TIMEOUT":
            pattern_logs = [{'patterns': ['PE CSP timed out on interface %{DATA:interfaceName}.'],
                             'log_explanation': 'PE CSP协议超时，PEX设备和父设备无法建立连接',
                             'log_recommended_action': '请检查父设备和PEX之间链路和IRF3.1相关配置'}]


    elif module == "PFILTER":

        if log_type_desc == "PFILTER_GLB_RES_CONFLICT":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} to the %{DATA:trafficDirection} direction globally. %{DATA:aclType} ACL %{NUMBER:aclNumber:int} has already been applied globally.'],
                             'log_explanation': 'IPv4、IPv6、MAC类型的ACL在某方向上全局应用了，系统无法在此方向上全局应用或更新相同类型的ACL规则',
                             'log_recommended_action': '删除相同类型的ACL'}]

        elif log_type_desc == "PFILTER_GLB_IPV4_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv4 default action to the %{DATA:trafficDirection} direction globally. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在某个方向上全局应用或更新IPv4缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_GLB_IPV4_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv4 default action to the %{DATA:trafficDirection} direction globally.'],
                             'log_explanation': '因故障导致系统无法在某个方向上全局应用或更新IPv4缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_GLB_IPV6_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv6 default action to the %{DATA:trafficDirection} direction globally. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在某个方向上全局应用或更新IPv6缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_GLB_IPV6_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv6 default action to the %{DATA:trafficDirection} direction globally.'],
                             'log_explanation': '因故障导致系统无法在某个方向上全局应用或更新IPv6缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_GLB_MAC_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the MAC default action to the %{DATA:trafficDirection} direction globally. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在某个方向上全局应用或更新MAC缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_GLB_MAC_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the MAC default action to the %{DATA:trafficDirection} direction globally.'],
                             'log_explanation': '因故障导致系统无法在某个方向上全局应用或更新MAC缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_GLB_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction globally. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在某个方向上全局应用或更新ACL规则',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_GLB_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction globally. The ACL is not supported.'],
                             'log_explanation': '因系统不支持ACL规则而导致无法在某个方向上全局应用或更新ACL规则',
                             'log_recommended_action': '检查ACL规则并删除不支持的配置'}]

        elif log_type_desc == "PFILTER_GLB_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction globally.'],
                             'log_explanation': '因故障导致系统无法在某个方向上全局应用或更新ACL', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IF_IPV4_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv4 default action to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在接口的某个方向上应用或更新IPv4缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_IF_IPV4_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv4 default action to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}.'],
                             'log_explanation': '因故障系统无法在接口的某个方向上应用或更新IPv4缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IF_IPV6_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv6 default action to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在接口的某个方向上应用或更新IPv6缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_IF_IPV6_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv6 default action to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}.'],
                             'log_explanation': '因故障系统无法在接口的某个方向上应用或更新IPv6缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IF_MAC_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the MAC default action to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在接口的某个方向上应用或更新MAC缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_IF_MAC_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the MAC default action to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}.'],
                             'log_explanation': '因故障系统无法在接口的某个方向上应用或更新MAC缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IF_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在接口的某个方向上应用或更新ACL规则',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_IF_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. The ACL is not supported.'],
                             'log_explanation': '因系统不支持ACL规则而导致无法在接口的某个方向上应用或更新ACL规则',
                             'log_recommended_action': '检查ACL规则并删除不支持的配置'}]

        elif log_type_desc == "PFILTER_IF_RES_CONFLICT":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. %{DATA:aclType} ACL %{NUMBER:aclNumber:int} has already been applied to the interface.'],
                             'log_explanation': 'IPv4、IPv6、MAC类型的ACL在接口某方向上应用了，系统无法在此方向上应用或更新相同类型的ACL规则',
                             'log_recommended_action': '删除相同类型的ACL'}]

        elif log_type_desc == "PFILTER_IF_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}.'],
                             'log_explanation': '因故障系统无法在接口的某个方向上应用或更新ACL规则', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IPV4_FLOW_INFO":
            pattern_logs = [{'patterns': [
                'ACL %{DATA:aclNumberName} %{DATA:trafficDirection} %{DATA:destinationPacketFilterApplies} rule %{DATA:idContentAclRule} %{DATA:informationFirstPacketFlowMatchesRule}'],
                             'log_explanation': '报文过滤引用的IPv4高级ACL规则匹配的首个报文的信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IPV4_FLOWLOG_STATIS":
            pattern_logs = [{'patterns': [
                'ACL %{DATA:aclNumberName} %{DATA:trafficDirection} rule %{DATA:idContentAclRule} %{DATA:informationFirstPacketFlowMatchedRule}, %{NUMBER:numberPacketsMatchRule:int} packet\\(s\\).'],
                             'log_explanation': '报文过滤引用的IPv4 高级ACL规则匹配报文的信息和统计信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IPV6_FLOW_INFO":
            pattern_logs = [{'patterns': [
                'IPv6 ACL %{DATA:aclNumberName} %{DATA:trafficDirection} %{DATA:destinationPacketFilterApplies} rule %{DATA:idContentAclRule} %{DATA:informationFirstPacketFlowMatchesRule}'],
                             'log_explanation': '报文过滤引用的IPv6高级ACL规则匹配的首个报文的信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IPV6_FLOWLOG_STATIS":
            pattern_logs = [{'patterns': [
                'IPv6 ACL %{DATA:aclNumberName} %{DATA:trafficDirection} rule %{DATA:idContentAclRule} %{DATA:informationFirstPacketFlowMatchedRule}, %{NUMBER:numberPacketsMatchRule:int} packet\\(s\\).'],
                             'log_explanation': '报文过滤引用的IPv6高级ACL规则匹配报文的信息和统计信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_IPV6_STATIS_INFO":
            pattern_logs = [{'patterns': [
                '%{DATA:param0} \\(%{DATA:param1}\\): Packet-filter IPv6 %{NUMBER:param2:int} %{DATA:param3} %{DATA:param4} %{NUMBER:param5:int} packet\\(s\\).'],
                             'log_explanation': 'ACL规则在报文过滤日志发送周期结束后匹配的报文个数', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_MAC_FLOW_INFO":
            pattern_logs = [{'patterns': [
                'MAC ACL %{DATA:aclNumberName} %{DATA:trafficDirection} %{DATA:destinationPacketFilterApplies} rule %{DATA:idContentAclRule} %{DATA:informationFirstPacketMatchesRule}'],
                             'log_explanation': '报文过滤引用的二层ACL规则匹配的首个报文的信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_STATIS_INFO":
            pattern_logs = [{'patterns': [
                '%{DATA:destinationPacketFilterApplies} \\(%{DATA:trafficDirection}\\): Packet-filter %{NUMBER:aclNumberName:int} %{DATA:idContentAclRule} %{NUMBER:numberPacketsMatchedRule:int} packet\\(s\\).'],
                             'log_explanation': 'ACL规则在报文过滤日志发送周期结束后匹配的报文个数', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_VLAN_IPV4_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv4 default action to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在VLAN的某个方向上应用或更新IPv4缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_VLAN_IPV4_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv4 default action to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '因故障系统无法在VLAN的某个方向上应用或更新IPv4缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_VLAN_IPV6_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv6 default action to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在VLAN的某个方向上应用或更新IPv6缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_VLAN_IPV6_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the IPv6 default action to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '因故障系统无法在VLAN的某个方向上应用或更新IPv6缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_VLAN_MAC_DACT_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the MAC default action to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在VLAN的某个方向上应用或更新MAC缺省动作',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_VLAN_MAC_DACT_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh the MAC default action to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '因故障系统无法在VLAN的某个方向上应用或更新MAC缺省动作', 'log_recommended_action': '无'}]

        elif log_type_desc == "PFILTER_VLAN_NO_RES":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}. The resources are insufficient.'],
                             'log_explanation': '因硬件资源不足，系统无法在VLAN的某个方向上应用或更新ACL规则',
                             'log_recommended_action': '使用display qos-acl resource命令检查硬件资源使用情况'}]

        elif log_type_desc == "PFILTER_VLAN_NOT_SUPPORT":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}. The ACL is not supported.'],
                             'log_explanation': '因系统不支持ACL规则而导致无法在VLAN的某个方向上应用或更新ACL规则',
                             'log_recommended_action': '检查ACL规则并删除不支持的配置'}]

        elif log_type_desc == "PFILTER_VLAN_RES_CONFLICT":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}. %{DATA:aclType} ACL %{NUMBER:aclNumber:int} has already been applied to the VLAN.'],
                             'log_explanation': 'IPv4、IPv6、MAC类型的ACL已经在VLAN的某方向上应用了，系统无法在此方向上应用或更新相同类型的ACL规则',
                             'log_recommended_action': '删除相同类型的ACL'}]

        elif log_type_desc == "PFILTER_VLAN_UNK_ERR":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh %{DATA:aclType} ACL %{NUMBER:aclNumber:int} %{DATA:aclRuleId} to the %{DATA:trafficDirection} direction of VLAN %{NUMBER:vlanId:int}.'],
                             'log_explanation': '因故障系统无法在VLAN的某个方向上应用或更新ACL规则', 'log_recommended_action': '无'}]


    elif module == "PIM":

        if log_type_desc == "PIM_NBR_DOWN":
            pattern_logs = [{'patterns': [
                '%{DATA:vpnInstanceName}: Neighbor %{DATA:ipAddressPimNeighbor} \\(%{DATA:interfaceName}\\) is down.'],
                             'log_explanation': 'PIM邻居的状态变为down', 'log_recommended_action': '检查PIM配置是否错误，检查网络是否发生拥塞'}]

        elif log_type_desc == "PIM_NBR_UP":
            pattern_logs = [{'patterns': [
                '%{DATA:vpnInstanceName}: Neighbor %{DATA:ipAddressPimNeighbor} \\(%{DATA:interfaceName}\\) is up.'],
                             'log_explanation': 'PIM邻居的状态变为up', 'log_recommended_action': '无'}]


    elif module == "PING":

        if log_type_desc == "PING_STATISTICS":
            pattern_logs = [{'patterns': [
                '%{DATA:pingPing6} statistics for %{DATA:ipAddress}: %{NUMBER:numberSentEchoRequests:int} packets transmitted, %{NUMBER:numberReceivedEchoReplies:int} packets received, %{DATA:percentageNon-repliedPacketsTotalRequestPackets}% packet loss, round-trip min/avg/max/std-dev = %{DATA:minimumRound-tripDelay}/%{DATA:averageRound-tripDelay}/%{DATA:maximumRound-tripDelay}/%{DATA:standardDeviationRound-tripDelay} ms.'],
                             'log_explanation': '用户执行ping命令查看公网中对端是否可达',
                             'log_recommended_action': '如果没有收到报文，请检查接口是否DOWN，并查找路由表，看是否存在有效路由'}]

        elif log_type_desc == "PING_VPN_STATISTICS":
            pattern_logs = [{'patterns': [
                '%{DATA:pingPing6} statistics for %{DATA:ipAddress} in VPN instance %{DATA:vpnInstanceName} : %{NUMBER:numberSentEchoRequests:int} packets transmitted, %{NUMBER:numberReceivedEchoReplies:int} packets received, %{DATA:percentageNon-repliedPacketsTotalRequestPackets}% packet loss, round-trip min/avg/max/std-dev = %{DATA:minimumRound-tripDelay}/%{DATA:averageRound-tripDelay}/%{DATA:maximumRound-tripDelay}/%{DATA:standardDeviationRound-tripDelay} ms.'],
                             'log_explanation': '用户执行ping命令查看VPN中的对端是否可达',
                             'log_recommended_action': '如果没有收到报文，请检查接口是否DOWN，并查找路由表，看是否存在有效路由'}]


    elif module == "PKG":

        if log_type_desc == "PKG_BOOTLOADER_FILE_FAILED":
            pattern_logs = [{'patterns': ['Failed to execute the boot-loader file command.'],
                             'log_explanation': '用户执行boot-loader file命令配置设备下次启动时使用的软件包，操作失败',
                             'log_recommended_action': '请根据提示信息采取相应措施'}]

        elif log_type_desc == "PKG_BOOTLOADER_FILE_SUCCESS":
            pattern_logs = [{'patterns': ['Executed the boot-loader file command successfully.'],
                             'log_explanation': '用户执行boot-loader file命令配置设备下次启动时使用的软件包，操作成功',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "PKG_INSTALL_ACTIVATE_FAILED":
            pattern_logs = [{'patterns': ['Failed to execute the install activate command.'],
                             'log_explanation': '用户执行install activate命令用来激活或查看软件包，操作失败',
                             'log_recommended_action': '请根据提示信息采取相应措施'}]

        elif log_type_desc == "PKG_INSTALL_ACTIVATE_SUCCESS":
            pattern_logs = [{'patterns': ['Executed the install activate command successfully.'],
                             'log_explanation': '用户执行install activate命令用来激活或查看软件包，操作成功', 'log_recommended_action': '无'}]


    elif module == "PKI":

        if log_type_desc == "GET_CERT_FROM_CA_SERVER_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to get the CA or RA certificate from the CA server. Reason: %{DATA:failureReason}.'],
                             'log_explanation': '命令行从CA服务器获取CA/RA证书时失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "IMPORT_CERT_FAIL":
            pattern_logs = [{'patterns': ['Failed to import the certificate. Reason: %{DATA:failureReason}.'],
                             'log_explanation': '执行导入命令时可能的失败，原因为证书无效等', 'log_recommended_action': '无'}]

        elif log_type_desc == "REQUEST_CERT_FAIL":
            pattern_logs = [{'patterns': ['Failed to request certificate of domain %{DATA:pkiDomainName}.'],
                             'log_explanation': '为PKI域申请证书失败', 'log_recommended_action': '检查设备和CA服务器的配置和其间的网络'}]

        elif log_type_desc == "REQUEST_CERT_SUCCESS":
            pattern_logs = [{'patterns': ['Request certificate of domain %{DATA:pkiDomainName} successfully.'],
                             'log_explanation': '为PKI域申请证书成功', 'log_recommended_action': '无'}]

        elif log_type_desc == "RETRIEVE_CRL_FAIL":
            pattern_logs = [{'patterns': ['Failed to retrieve the CRL. Reason: %{DATA:failureReason}.'],
                             'log_explanation': '取回CRL时的失败原因', 'log_recommended_action': '无'}]

        elif log_type_desc == "VALIDATE_CERT_FAIL":
            pattern_logs = [{'patterns': ['Failed to validate the certificate. Reason: %{DATA:failureReason}.'],
                             'log_explanation': '执行验证命令时可能的失败，原因为证书无效等', 'log_recommended_action': '无'}]


    elif module == "PKT2CPU":

        if log_type_desc == "PKT2CPU_NO_RESOURCE":
            pattern_logs = [{'patterns': [
                'The resources are insufficient.\n-Interface=%{DATA:param3}-ProtocolType=%{NUMBER:param4:int}-SrcPort=%{NUMBER:param5:int}-DstPort=%{NUMBER:param6:int}; The resources are insufficient.'],
                             'log_explanation': '硬件资源不足', 'log_recommended_action': '取消配置'}]


    elif module == "PKTCPT":

        if log_type_desc == "PKTCPT_AP_OFFLINE":
            pattern_logs = [{'patterns': ['Failed to start packet capture. Reason: AP was offline.'],
                             'log_explanation': '指定报文捕获的AP没有上线，报文捕获启动失败',
                             'log_recommended_action': '检查配置，AP上线后再次开启报文捕获'}]

        elif log_type_desc == "PKTCPT_AREADY_EXIT":
            pattern_logs = [{'patterns': [
                'Failed to start packet capture. Reason: The AP was uploading frames captured during the previous capturing operation.'],
                             'log_explanation': 'AC/FIT AP组网，当AC上的报文捕获功能先停止时，AP还在上传捕获的报文。此时用户再次开启报文捕获功能，报文捕获功能会启动失败',
                             'log_recommended_action': '请稍后重新开启报文捕获功能'}]

        elif log_type_desc == "PKTCPT_CONN_FAIL":
            pattern_logs = [
                {'patterns': ['Failed to start packet capture. Reason: Failed to connect to the FTP server.'],
                 'log_explanation': '无法连接到与设备在同一网段的FTP服务器，报文捕获功能启动失败',
                 'log_recommended_action': '·          检查URL是否合法。可能情况包括：指定的FTP服务器的IP地址不存在；指定的IP地址不是FTP服务器的地址；指定的FTP服务器的接口处于关闭状态\n·          检查URL中域名解析是否成功\n·          检查开启报文捕获服务设备与FTP服务器是否可达\n·          检查FTP服务器是否上线'}]

        elif log_type_desc == "PKTCPT_INVALD_FILTER":
            pattern_logs = [{'patterns': [
                'Failed to start packet capture. Reason: Invalid expression for matching packets to be captured.'],
                             'log_explanation': '捕获过滤规则非法，启动报文捕获功能失败', 'log_recommended_action': '修改捕获过滤规则'}]

        elif log_type_desc == "PKTCPT_LOGIN_DENIED":
            pattern_logs = [{'patterns': ['Packet capture aborted. Reason: FTP server login failure.'],
                             'log_explanation': '登录FTP服务器失败，报文捕获退出', 'log_recommended_action': '检查用户名密码是否正确'}]

        elif log_type_desc == "PKTCPT_MEMORY_ALERT":
            pattern_logs = [{'patterns': ['Packet capture aborted. Reason: Memory threshold reached.'],
                             'log_explanation': '设备达到内存门限时，报文捕获功能退出', 'log_recommended_action': '无'}]

        elif log_type_desc == "PKTCPT_OPEN_FAIL":
            pattern_logs = [
                {'patterns': ['Failed to start packet capture. Reason: File for storing captured frames not opened.'],
                 'log_explanation': '将报文文件保存到FLASH时，文件路径无法打开，报文捕获功能启动失败',
                 'log_recommended_action': '·          若用户不具有写文件权限，请配置写权限\n·          若指定的文件名是已经存在并被其它程序占用，请使用其它文件名'}]

        elif log_type_desc == "PKTCPT_OPERATION_TIMEOUT":
            pattern_logs = [{'patterns': ['Failed to start or continue packet capture. Reason: Operation timed out.'],
                             'log_explanation': '由于指定的与设备在不同网段的FTP服务器不可达，连接超时导致报文捕获启动失败；由于指定的与设备在不同网段的FTP服务器不在线，上传捕获的报文超时，导致报文捕获退出',
                             'log_recommended_action': '·          检查FTP服务器是否可达\n·          检查FTP服务器是否在线'}]

        elif log_type_desc == "PKTCPT_SERVICE_FAIL":
            pattern_logs = [{'patterns': ['Failed to start packet capture. Reason: TCP or UDP port binding faults.'],
                             'log_explanation': '由于TCP或者UDP端口绑定冲突等原因导致报文捕获功能启动失败',
                             'log_recommended_action': '·          如果之前打开的报文捕获客户端（第三方软件wireshark）没有关闭，请关闭后重新启动报文捕获功能\n·          绑定新的端口号，重新启动报文捕获功能'}]

        elif log_type_desc == "PKTCPT_UNKNOWN_ERROR":
            pattern_logs = [{'patterns': ['Failed to start or continue packet capture. Reason: Unknown error.'],
                             'log_explanation': '其它未知原因导致服务启动失败或者退出', 'log_recommended_action': '无'}]

        elif log_type_desc == "PKTCPT_UPLOAD_ERROR":
            pattern_logs = [{'patterns': ['Packet capture aborted. Reason: Failed to upload captured frames.'],
                             'log_explanation': '由于上传捕获的数据报文失败，导致报文捕获退出',
                             'log_recommended_action': '·          检查是否试图改变FTP的工作目录\n·          检查指定FTP服务器上文件是否有写权限\n·          检查FTP服务器是否下线\n·          检查与FTP服务器是否可达\n·          检查FTP服务器是否已满\n·          检查报文捕获服务是否退出'}]

        elif log_type_desc == "PKTCPT_WRITE_FAIL":
            pattern_logs = [{'patterns': ['Packet capture aborted. Reason: Not enough space to store captured frames.'],
                             'log_explanation': '报文文件保存到FLASH时，FLASH已满，报文捕获功能退出',
                             'log_recommended_action': '删除无用文件释放磁盘空间'}]


    elif module == "POE":

        if log_type_desc == "POE_AI_CLEAR":
            pattern_logs = [{'patterns': [
                'Clearing all preceding AI configurations on PoE port %{DATA:param0}. Reason: The port still cannot supply power to the PD after forced power supply has been enabled on the port.'],
                             'log_explanation': '开启PoE接口强制供电，处于未供电状态，清除之前的所有AI PoE配置',
                             'log_recommended_action': '请检查PoE接口到PD之间的链路是否存在硬件故障'}]

        elif log_type_desc == "POE_AI_DETECTIONMODE_NONE":
            pattern_logs = [{'patterns': [
                'Changing the PD detection mode for PoE port %{DATA:piName} to none. Reason: The port still cannot supply power to the PD after the PD detection mode has been changed to simple.'],
                             'log_explanation': '修改对PD支持标准的检测方式为简单检测方式仍无法恢复PoE供电，修改对PD支持标准的检测方式为不检测尝试恢复PoE供电',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_DETECTIONMODE_SIMPLE":
            pattern_logs = [{'patterns': [
                'Changing the PD detection mode for PoE port %{DATA:param0} to simple. Reason: The port still cannot supply power to the PD after non-standard PD detection is enabled.'],
                             'log_explanation': '开启接口的非标准PD检测功能仍无法恢复PoE供电，修改对PD支持标准的检测方式为简单检测方式尝试恢复PoE供电',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_DISCONNET_AC":
            pattern_logs = [{'patterns': [
                'Changing from MPS detection to AC detection on PoE port %{DATA:piName}. Reason: The port still cannot supply power to the PD after MPS detection is delayed.'],
                             'log_explanation': '延迟启动MPS电流检测时间无法恢复PoE接口供电，切换MPS电流检测为AC检测',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_DISCONNET_DELAY":
            pattern_logs = [{'patterns': [
                'Delaying the MPS detection on PoE port %{DATA:param0}. Reason: The port has stopped power supply because of MPS current insufficiency.'],
                             'log_explanation': 'PoE接口处于供电状态的情况下发生掉电时，系统检测到掉电原因为MPS电流过小导致PSE认为PD已经拔出而关断电压输出，则延迟启动MPS电流检测时间尝试恢复供电',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_FORCE_PoE":
            pattern_logs = [{'patterns': [
                'Enabling forced power supply on PoE port %{DATA:piName}. Reason: The port still cannot supply power to the PD after the PD detection mode has been changed to none.'],
                             'log_explanation': '修改对PD支持标准的检测方式为不检测仍无法恢复PoE供电，开启PoE接口强制供电',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_HIGH_INRUSH":
            pattern_logs = [{'patterns': [
                'Increasing the inrush current threshold for PoE port %{DATA:param0}. Reason: The port has stopped power supply because of a high inrush current.'],
                             'log_explanation': 'PoE接口处于供电状态的情况下发生掉电时，系统检测到掉电原因为Inrush冲击电流过大，自动提高Inrush冲击电流阈值允许高冲击电流通过',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_LEGACY":
            pattern_logs = [{'patterns': [
                'Enabling non-standard PD detection on PoE port %{DATA:param0}. Reason: The port cannot supply power to the PD.'],
                             'log_explanation': '检测到PoE接口未进入供电状态，开启接口的非标准PD检测功能尝试恢复PoE供电',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_MAXPOWER":
            pattern_logs = [{'patterns': [
                'Increasing the maximum power of PoE port %{DATA:param0} to %{NUMBER:param1:int}. Reason: An instant power surge has caused overload self-protection of the port'],
                             'log_explanation': 'PoE接口处于供电状态的情况下发生掉电时，系统检测到掉电原因为瞬间功率过大导致过载保护，提高PoE接口的最大供电功率',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "POE_AI_RESTART":
            pattern_logs = [{'patterns': [
                'Re-enabling PoE on port %{DATA:param0}. Reason: The power consumption of the port is 0.'],
                             'log_explanation': 'PoE接口处于供电状态，但功率消耗为0，复位接口的PoE供电功能', 'log_recommended_action': '无'}]


    elif module == "PORTAL":

        if log_type_desc == "PORTAL_RULE_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to assign a portal rule. Reason=%{DATA:reasonRuleAssignmentFailure}.'],
                 'log_explanation': 'Portal规则下发失败', 'log_recommended_action': '请根据规则下发失败的原因选择相应的处理方式，详见表1-1'}]


    elif module == "PORTSEC":

        if log_type_desc == "PORTSEC_ACL_FAILURE":
            pattern_logs = [{'patterns': ['ACL authorization failed because%{DATA:causeFailure}.'],
                             'log_explanation': '下发授权ACL失败，及其原因', 'log_recommended_action': '根据失败原因修改配置'}]

        elif log_type_desc == "PORTSEC_CAR_FAILURE":
            pattern_logs = [
                {'patterns': ['Failed to assign CAR attributes to driver.'], 'log_explanation': '下发CAR到驱动失败',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "PORTSEC_CREATEAC_FAILURE":
            pattern_logs = [{'patterns': ['Failed to map an Ethernet service instance to the VSI.'],
                             'log_explanation': '端口安全模块接收到相关授权信息或者从其子线程模块收到将以太网服务实例与VSI绑定的信息后，执行该操作，如果操作失败则输出此日志信息',
                             'log_recommended_action': '使用display l2vpn vsi命令查询VSI Name是否存在，如果不存在，请通过vsi命令创建对应的VSI'}]

        elif log_type_desc == "PORTSEC_LEARNED_MACADDR":
            pattern_logs = [{'patterns': ['A new MAC address was learned.'], 'log_explanation': '学到一个新的安全MAC地址',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "PORTSEC_NTK_NOT_EFFECTIVE":
            pattern_logs = [{'patterns': [
                'The NeedToKnow feature is configured but is not effective on interface %{DATA:interfaceTypeNumber}.'],
                             'log_explanation': 'NeedToKnow模式在接口上不生效，因为该接口不支持NeedToKnow模式',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "PORTSEC_PORTMODE_NOT_EFFECTIVE":
            pattern_logs = [{'patterns': [
                'The port security mode is configured but is not effective on interface %{DATA:interfaceTypeNumber}.'],
                             'log_explanation': '端口安全模式在接口上不生效，因为该接口不支持这种端口安全模式',
                             'log_recommended_action': '改变端口安全模式或关闭接口的端口安全特性'}]

        elif log_type_desc == "PORTSEC_PROFILE_FAILURE":
            pattern_logs = [
                {'patterns': ['Failed to assign a user profile to driver.'], 'log_explanation': '下发User Profile到驱动失败',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "PORTSEC_URL_FAILURE":
            pattern_logs = [
                {'patterns': ['URL authorization failed because %{DATA:param2}.'], 'log_explanation': '下发授权URL失败',
                 'log_recommended_action': '根据失败原因修改配置'}]

        elif log_type_desc == "PORTSEC_VIOLATION":
            pattern_logs = [{'patterns': ['Intrusion protection was triggered.'], 'log_explanation': '触发入侵检测',
                             'log_recommended_action': '检查配置情况或改变端口安全模式'}]

        elif log_type_desc == "PORTSEC_VLANMACLIMIT":
            pattern_logs = [{'patterns': ['Maximum number of MAC addresses already reached in the VLAN.'],
                             'log_explanation': 'VLAN内同时接入的MAC地址数量达到上限，不允许新MAC地址用户接入',
                             'log_recommended_action': '检查是否存在来自未知源MAC的报文攻击端口'}]


    elif module == "PPP":

        if log_type_desc == "IPPOOL_ADDRESS_EXHAUSTED":
            pattern_logs = [{'patterns': ['The address pool %{DATA:poolName} was exhausted.'],
                             'log_explanation': '当地址池里最后一个地址分配出去时，打印本信息', 'log_recommended_action': '向地址池里添加地址'}]

        elif log_type_desc == "PPP_USER_LOGOFF":
            pattern_logs = [
                {'patterns': ['User logged off.'], 'log_explanation': '用户下线', 'log_recommended_action': '无'}]

        elif log_type_desc == "PPP_USER_LOGON_FAILED":
            pattern_logs = [{'patterns': ['User got online failed.'], 'log_explanation': '用户上线失败',
                             'log_recommended_action': '·          检查用户名和密码是否正确\n·          检查认证和计费服务器是否工作正常\n·          检查设备上地址池是否配置正确'}]

        elif log_type_desc == "PPP_USER_LOGON_SUCCESS":
            pattern_logs = [{'patterns': ['User got online successfully.'], 'log_explanation': '用户上线成功',
                             'log_recommended_action': '无'}]


    elif module == "PTP":

        if log_type_desc == "PTP_MASTER_CLOCK_CHANGE":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP master clock property changed. \\(OldMasterClockId=%{DATA:param1}, CurrentMasterClockId=%{DATA:param2}, NewSourceIfIndex=%{NUMBER:param3:int}, OldSourcePortNum=%{NUMBER:param4:int}, CurrentSourcePortNum=%{NUMBER:param5:int}, OldSourcePortName=%{DATA:param6}, CurrentSourcePortName=%{DATA:param7}\\)'],
                             'log_explanation': '主时钟源属性发生改变，原因包括：\n·          PTP域内的时钟设备属性发生变化，导致出现了优先级更高的时钟源或获取时钟源的路径发生了改变\n·          接入了优先级更高的时钟源\n·          接收时钟源信号的PTP接口所在链路故障或者PTP接口DOWN',
                             'log_recommended_action': '使用display ptp interface brief命令查看是否存在PTP接口处于Disabled状态\n·          若存在接口处于Disabled状态，则表示该状态为PTP协议的错误状态（即检测到错误），接口不处理PTP协议报文；收集告警、日志和配置信息，联系技术支持\n·          若不存在接口处于Disabled状态，则查看PTP配置信息是否发生改变\n¡  若PTP配置信息发生改变，则恢复配置\n¡  若PTP配置信息未发生改变，则收集告警、日志和配置信息，联系技术支持'}]

        elif log_type_desc == "PTP_PKTLOST":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP packets were lost. \\(PortName=%{DATA:param1}, PktType=%{DATA:param2}\\)'],
                             'log_explanation': 'Slave端口检测Announce、Delay_Resp、Sync报文，超过检测时间没有收到报文，则认为报文丢失',
                             'log_recommended_action': '在打印该日志的PTP从时钟设备上使用display ptp statistics命令查看接收报文统计计数是否增长\n·          若增长，则表示链路延时过长导致的超时，无须处理\n·          若不增长，则在PTP主时钟设备使用display ptp statistics命令查看发送报文统计计数是否增长\n¡  若增长，则表示链路故障导致对端超时没收到报文，排除故障恢复链路\n¡  若不增长，则收集告警、日志和配置信息，联系技术支持'}]

        elif log_type_desc == "PTP_PKTLOST_RECOVER":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP packets lost were recovered. \\(PortName=%{DATA:param1}, PktType=%{DATA:param2}\\)'],
                             'log_explanation': '从PTP报文丢失告警状态中恢复正常。只有当Slave端口检测Announce、Delay_Resp、Sync报文超时后又重新收到Announce、Delay_Resp报文或者超时时间过长设备自身由从时钟转变为主时钟时，才会打印此日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "PTP_PORT_BMCINFO_CHANGE":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP BMC info for port %{NUMBER:param1:int} changed. \\(PortName=%{DATA:param2}, PortSourceId=%{DATA:param3}, PortSourcePortNum=%{NUMBER:param4:int}, PortSourceStepsRemoved=%{NUMBER:param5:int}, CurrentMasterClockId=%{DATA:param6}\\)'],
                             'log_explanation': 'PTP接口收到的时钟源ID、时钟源端口号或时钟源跳数等时钟源信息发生变化', 'log_recommended_action': '无'}]

        elif log_type_desc == "PTP_PORT_STATE_CHANGE":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP port state changed. \\(IfIndex=%{NUMBER:param1:int}, PortName=%{DATA:param2}, PortState=%{DATA:param3}, OldPortState=%{DATA:param4}\\)'],
                             'log_explanation': 'PTP接口状态发生改变，原因包括：\n·          PTP域内的时钟设备属性发生变化，比如优先级、时钟等级、时钟精度、接口的NotSlave属性等\n·          接入了优先级更高的时钟源\n·          PTP接口所在链路故障或者PTP接口DOWN',
                             'log_recommended_action': '使用display ptp interface brief命令查看是否存在PTP接口处于Fault状态\n·          若存在接口处于Fault状态，则表示链路故障或接口DOWN，排除故障恢复链路\n·          若不存在接口处于Fault状态，则查看PTP配置信息是否发生改变\n¡  若PTP配置信息发生改变，则恢复配置\n¡  若PTP配置信息未发生改变，则收集告警、日志和配置信息，联系技术支持'}]

        elif log_type_desc == "PTP_SRC_CHANGE":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP clock source property changed. \\(SourceName=%{DATA:param1}, Priority1=%{NUMBER:param2:int}, Priority2=%{NUMBER:param3:int}, ClockClass=%{NUMBER:param4:int}, ClockAccuracy=%{NUMBER:param5:int}], ClockSourceType=%{DATA:param6}\\)'],
                             'log_explanation': '时钟源属性发生改变，原因包括：\n·          用户通过命令行改变时钟源属性\n·          接收到了精度更高的外接时钟源',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "PTP_SRC_SWITCH":
            pattern_logs = [{'patterns': [
                'In PTP instance %{NUMBER:param0:int}, PTP clock source switched. \\(LastClockID=%{DATA:param1}, CurrentClockID=%{DATA:param2}\\)'],
                             'log_explanation': '新的更好的时钟源加入PTP域，设备跟踪的时钟源发生切换', 'log_recommended_action': '无'}]

        elif log_type_desc == "PTP_TIME_LOCK":
            pattern_logs = [{'patterns': ['Time resumed to locked state.'], 'log_explanation': '时钟从失锁状态中恢复为正常',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "PTP_TIME_NOT_LOCK":
            pattern_logs = [{'patterns': ['Time not in locked state.'],
                             'log_explanation': '时钟失锁告警，原因包括：\n·          频率失锁\n·          子卡或者时钟扣板故障\n·          DSP收到的时间戳不变或者错误',
                             'log_recommended_action': '检查PTP Slave接口是否链路故障或接口DOWN：\n·          若链路故障或接口DOWN，排除故障恢复链路\n·          接口正常，则查看PTP配置信息是否发生改变\n¡  若PTP配置信息发生改变，则恢复配置\n¡  若PTP配置信息未发生改变，则收集告警、日志和配置信息，联系技术支持'}]


    elif module == "QOS":

        if log_type_desc == "MIRROR_SYNC_CFG_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to restore configuration for monitoring group %{NUMBER:monitoringGroup:int} in %{DATA:chassisNumberPlusSlotNumberSlotNumber}, because %{DATA:failureCause}'],
                             'log_explanation': '业务板插入设备后，恢复该业务板监控组数据失败。失败原因如下：\n·          监控端口总数超过当前监控组支持的最大数量\n·          当前业务板监控资源不足\n·          监控组中端口的类型在当前业务板不支持',
                             'log_recommended_action': '删除或者修改不支持配置'}]

        elif log_type_desc == "QOS_CAR_APPLYUSER_FAIL":
            pattern_logs = [{'patterns': [
                '%{DATA:userIdentity}; Failed to apply the %{DATA:applicationDirection} CAR in %{DATA:profileType} profile %{DATA:profileName} to the user. Reason: %{DATA:failureCause}.'],
                             'log_explanation': '1.用户上线，下发配置的CAR信息失败\n2.用户已经上线，修改CAR信息或者增加CAR应用失败',
                             'log_recommended_action': '取消CAR在profile下的应用或者修改CAR的相关参数信息'}]

        elif log_type_desc == "QOS_CBWFQ_REMOVED":
            pattern_logs = [{'patterns': ['CBWFQ is removed from %{DATA:interfaceName}.'],
                             'log_explanation': '因接口最大带宽或接口速率更改后低于接口上原来配置的CBWFQ要求的带宽或速率，系统从接口上删除CBWFQ',
                             'log_recommended_action': '增大接口最大带宽或接口速率后重新应用被删除的CBWFQ'}]

        elif log_type_desc == "QOS_GTS_APPLYUSER_FAIL":
            pattern_logs = [{'patterns': [
                '%{DATA:userIdentity}; Failed to apply GTS in user profile %{DATA:userProfileName} to the user. Reason: %{DATA:failureCause}.'],
                             'log_explanation': '1.用户上线，下发配置的GTS信息失败\n2.用户已经上线，修改GTS信息或者增加GTS应用失败',
                             'log_recommended_action': '取消GTS在user profile下的应用或者修改GTS的相关参数信息'}]

        elif log_type_desc == "QOS_LR_APPLYIF_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply the rate limit on interface %{DATA:interfaceName}. Reason: %{DATA:failureCause}'],
                             'log_explanation': '·          不支持在接口上配置限速\n·          由于资源不足，导致在接口上配置限速失败',
                             'log_recommended_action': '请根据失败原因，取消接口上的限速配置或者修改接口限速的相关配置'}]

        elif log_type_desc == "QOS_NOT_ENOUGH_BANDWIDTH":
            pattern_logs = [{'patterns': [
                'Policy %{DATA:policyName} requested bandwidth %{NUMBER:requiredBandwidthCbwfq:int}\\(kbps\\). Only %{NUMBER:availableBandwidthInterface:int}\\(kbps\\) is available on %{DATA:interfaceName}.'],
                             'log_explanation': '因CBWFQ要求的带宽大于接口最大带宽，CBWFQ配置失败',
                             'log_recommended_action': '增大接口最大带宽值或减小CBWFQ要求的带宽值'}]

        elif log_type_desc == " QOS_NOT_ENOUGH_NNIBANDWIDTH":
            pattern_logs = [{'patterns': [
                'The total UNI bandwidth is greater than the NNI bandwidth.\nThe total UNI bandwidth is greater than the NNI bandwidth.The bandwidth of %{DATA:param0} is changed.\nThe total UNI bandwidth is greater than the NNI bandwidth.%{DATA:param1} is created based on %{DATA:param2} of the UNI interface.'],
                             'log_explanation': '·          当用户增加上行接口带宽或降低下行接口带宽限速后，下行总带宽仍然大于上行带宽\n·          接口带宽改变导致下行接口总带宽大于上行接口总带宽\n·          新创建的动态子接口导致下行接口总带宽大于上行接口总带宽',
                             'log_recommended_action': '增加上行接口带宽或降低下行接口带宽限速'}]

        elif log_type_desc == "QOS_POLICY_APPLYCOPP_CBFAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply classifier-behavior %{DATA:nameClassifier-behaviorAssociation} in policy %{DATA:policyName} to the %{DATA:applicationDirection} direction of control plane slot %{NUMBER:slotNumber:int}. %{DATA:failureCause}.'],
                             'log_explanation': '系统在控制平面的某个方向上应用或更新QoS策略中的某个CB对失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYCOPP_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh QoS policy %{DATA:policyName} to the %{DATA:trafficDirection} direction of control plane slot %{NUMBER:slotNumber:int}. %{DATA:failureCause}.'],
                             'log_explanation': '系统在控制平面的某个方向上应用或更新QoS策略失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYGLOBAL_CBFAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply classifier-behavior %{DATA:nameClassifier-behaviorAssociation} in policy %{DATA:policyName} to the %{DATA:trafficDirection} direction globally. %{DATA:failureCause}.'],
                             'log_explanation': '系统在某个方向上全局应用或更新QoS策略中的某个CB对失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYGLOBAL_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh QoS policy %{DATA:policyName} to the %{DATA:trafficDirection} direction globally. %{DATA:failureCause}.'],
                             'log_explanation': '系统在某个方向上全局应用或更新QoS策略失败', 'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYIF_CBFAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply classifier-behavior %{DATA:param0} in policy %{DATA:param1} to the %{DATA:param2} direction of interface %{DATA:param3}. %{DATA:param4}.'],
                             'log_explanation': '系统在接口的某个方向上应用或更新QoS策略中的某个CB对失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYIF_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh QoS policy %{DATA:policyName} to the %{DATA:trafficDirection} direction of interface %{DATA:interfaceName}. %{DATA:failureCause}.'],
                             'log_explanation': '系统在接口的某个方向上应用或更新QoS策略失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYUSER_FAIL":
            pattern_logs = [{'patterns': [
                '%{DATA:userIdentity}; Failed to apply the %{DATA:applicationDirection} QoS policy %{DATA:qosPolicyName} in user profile %{DATA:userProfileName} to the user.Reason: %{DATA:failureCause}.'],
                             'log_explanation': '1.用户上线，下发配置的QoS policy信息失败\n2.用户已经上线，修改QoS Policy信息或者增加QoS Policy应用失败',
                             'log_recommended_action': '取消QoS policy在User profile下的应用或者修改QoS Profile的信息'}]

        elif log_type_desc == "QOS_POLICY_APPLYVLAN_CBFAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply classifier-behavior %{DATA:param0} in policy %{DATA:param1} to the %{DATA:param2} direction of VLAN %{NUMBER:param3:int}. %{DATA:param4}.'],
                             'log_explanation': '系统在VLAN的某个方向上应用或更新QoS策略中的某个CB对失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_POLICY_APPLYVLAN_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply or refresh QoS policy %{DATA:policyName} to the %{DATA:applicationDirection} direction of VLAN %{NUMBER:vlanId:int}. %{DATA:failureCause}.'],
                             'log_explanation': '系统在VLAN的某个方向上应用或更新QoS策略失败',
                             'log_recommended_action': '请根据失败原因，修改策略中的配置'}]

        elif log_type_desc == "QOS_QMPROFILE_APPLYIF_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply queue management profile %{DATA:queueSchedulingProfileName} on interface %{DATA:interfaceName}. Reason: %{DATA:failureCause}'],
                             'log_explanation': '·          不支持在接口上应用队列调度策略\n·          由于资源不足，导致在接口上应用队列调度策略失败',
                             'log_recommended_action': '请根据失败原因，取消队列调度策略在接口上的应用或者修改队列调度策略的相关配置'}]

        elif log_type_desc == "QOS_QMPROFILE_APPLYUSER_FAIL":
            pattern_logs = [{'patterns': [
                '%{DATA:userIdentity}; Failed to apply queue management profile %{DATA:queueSchedulingProfileName} in session group profile %{DATA:sessionGroupProfileName} to the user. Reason: %{DATA:failureCause}.'],
                             'log_explanation': '1.用户上线，下发配置的QMProfile信息失败\n2.用户已经上线，修改QMProfile信息或者增加QMProfile应用失败',
                             'log_recommended_action': '取消QMProfile在Session group profile下的应用或者修改QMProfile的相关信息'}]

        elif log_type_desc == "QOS_QMPROFILE_MODIFYQUEUE_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to configure queue %{NUMBER:queueId:int} in queue management profile %{DATA:profileName}. %{DATA:failureCause}.'],
                             'log_explanation': 'qmprofile成功应用到端口后，再对某队列进行修改，新的参数超出端口能力范围',
                             'log_recommended_action': '取消此profile在对应板的应用再修改队列参数'}]

        elif log_type_desc == "QOS_QUEUE_APPLYIF_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to apply queue scheduling on interface %{DATA:interfaceName}. Reason: %{DATA:failureCause}'],
                             'log_explanation': '·          不支持在接口上进行队列配置\n·          由于资源不足，导致在接口上进行队列配置失败',
                             'log_recommended_action': '请根据失败原因，取消接口上的队列配置或者修改队列配置的相关配置'}]

        elif log_type_desc == " QOS_NNIBANDWIDTH_OVERFLOW":
            pattern_logs = [{'patterns': [
                'Failed to restore the UNI configuration of %{DATA:interfaceName}, because the total UNI bandwidth is greater than the NNI bandwidth.'],
                             'log_explanation': '恢复下行接口时，因下行接口上的CAR限速总和超过上行接口带宽，接口的下行接口功能恢复失败',
                             'log_recommended_action': '增加上行接口带宽或降低下行接口CAR限速总和后，重新使能下行口功能'}]

        elif log_type_desc == "WRED_TABLE_CFG_FAIL":
            pattern_logs = [{'patterns': [
                'Failed to dynamically modify the configuration of WRED table %{DATA:wredTableName}, because %{DATA:failureCause}.'],
                             'log_explanation': '由于各业务板支持特性不同，某些配置在部分业务板上不支持', 'log_recommended_action': '无'}]


    elif module == "RADIUS":

        if log_type_desc == "RADIUS_ACCT_SERVER_DOWN":
            pattern_logs = [{'patterns': [
                'RADIUS accounting server was blocked: Server IP=%{DATA:ipAddressAccountingServer}, port=%{NUMBER:portNumberAccountingServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'RADIUS计费服务器状态为阻塞',
                             'log_recommended_action': '1.      检查RADIUS服务器是否开启。如果RADIUS服务器关闭，请重新启动RADIUS服务器。\n2.      执行ping命令检查RADIUS服务器是否可达。如果RADIUS服务器不可达，请检查链路是否通畅。\n3.      请收集日志信息和诊断信息，并联系技术支持。'}]

        elif log_type_desc == "RADIUS_ACCT_SERVER_UP":
            pattern_logs = [{'patterns': [
                'RADIUS accounting server became active: Server IP=%{DATA:ipAddressAccountingServer}, port=%{NUMBER:portNumberAccountingServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'RADIUS计费服务器状态为激活', 'log_recommended_action': '无'}]

        elif log_type_desc == "RADIUS_AUTH_SERVER_DOWN":
            pattern_logs = [{'patterns': [
                'RADIUS authentication server was blocked: Server IP=%{DATA:ipAddressAuthenticationServer}, port=%{NUMBER:portNumberAuthenticationServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'RADIUS认证服务器状态为阻塞',
                             'log_recommended_action': '4.      检查RADIUS服务器是否开启。如果RADIUS服务器关闭，请重新启动RADIUS服务器。\n5.      执行ping命令检查RADIUS服务器是否可达。如果RADIUS服务器不可达，请检查链路是否通畅。\n6.      请收集日志信息和诊断信息，并联系技术支持'}]

        elif log_type_desc == "RADIUS_AUTH_SERVER_UP":
            pattern_logs = [{'patterns': [
                'RADIUS authentication server became active: Server IP=%{DATA:ipAddressAuthenticationServer}, port=%{NUMBER:portNumberAuthenticationServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'RADIUS认证服务器状态为激活', 'log_recommended_action': '无'}]


    elif module == "TACACS":

        if log_type_desc == "TACACS_AUTH_FAILURE":
            pattern_logs = [{'patterns': ['User %{DATA:username} at %{DATA:ipAddress} failed authentication.'],
                             'log_explanation': 'TACACS 服务器了拒绝用户的认证请求', 'log_recommended_action': '无'}]

        elif log_type_desc == "TACACS_AUTH_SUCCESS":
            pattern_logs = [{'patterns': ['User %{DATA:username} at %{DATA:ipAddress} was authenticated successfully.'],
                             'log_explanation': 'TACACS 服务器接收了用户的认证请求', 'log_recommended_action': '无'}]

        elif log_type_desc == "TACACS_REMOVE_SERVER_FAIL":
            pattern_logs = [{'patterns': ['Failed to remove servers in scheme %{DATA:schemeName}.'],
                             'log_explanation': '删除TACACS方案中的服务器失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "TACACS_ACCT_SERVER_DOWN":
            pattern_logs = [{'patterns': [
                'TACACS accounting server was blocked: Server IP=%{DATA:ipAddressAccountingServer}, port=%{NUMBER:portNumberAccountingServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'TACACS计费服务器状态为阻塞',
                             'log_recommended_action': '1.      检查TACACS服务器是否开启。如果TACACS服务器关闭，请重新启动TACACS服务器。\n2.      执行ping命令检查TACACS服务器是否可达。如果TACACS服务器不可达，请检查链路是否通畅。\n3.      请收集日志信息和诊断信息，并联系技术支持'}]

        elif log_type_desc == "TACACS_ACCT_SERVER_UP":
            pattern_logs = [{'patterns': [
                'TACACS accounting server became active: Server IP=%{DATA:ipAddressAccountingServer}, port=%{NUMBER:portNumberAccountingServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'TACACS计费服务器状态为激活', 'log_recommended_action': '无'}]

        elif log_type_desc == "TACACS_AUTH_SERVER_DOWN":
            pattern_logs = [{'patterns': [
                'TACACS authentication server was blocked: Server IP=%{DATA:ipAddressAuthenticationServer}, port=%{NUMBER:portNumberAuthenticationServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'TACACS认证服务器状态为阻塞',
                             'log_recommended_action': '1.      检查TACACS服务器是否开启。如果TACACS服务器关闭，请重新启动TACACS服务器。\n2.      执行ping命令检查TACACS服务器是否可达。如果TACACS服务器不可达，请检查链路是否通畅。\n3.      请收集日志信息和诊断信息，并联系技术支持'}]

        elif log_type_desc == "TACACS_AUTH_SERVER_UP":
            pattern_logs = [{'patterns': [
                'TACACS authentication server became active: Server IP=%{DATA:ipAddressAuthenticationServer}, port=%{NUMBER:portNumberAuthenticationServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'TACACS认证服务器状态为激活', 'log_recommended_action': '无'}]

        elif log_type_desc == "TACACS_AUTHOR_SERVER_DOWN":
            pattern_logs = [{'patterns': [
                'TACACS authorization server was blocked: Server IP=%{DATA:ipAddressAuthorizationServer}, port=%{NUMBER:portNumberAuthorizationServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'TACACS授权服务器状态为阻塞',
                             'log_recommended_action': '1.      检查TACACS服务器是否开启。如果TACACS服务器关闭，请重新启动TACACS服务器。\n2.      执行ping命令检查TACACS服务器是否可达。如果TACACS服务器不可达，请检查链路是否通畅。\n3.      请收集日志信息和诊断信息，并联系技术支持'}]

        elif log_type_desc == "TACACS_AUTHOR_SERVER_UP":
            pattern_logs = [{'patterns': [
                'TACACS authorization server became active: Server IP=%{DATA:ipAddressAuthorizationServer}, port=%{NUMBER:portNumberAuthorizationServer:int}, VPN instance=%{DATA:vpnInstanceName}.'],
                             'log_explanation': 'TACACS授权服务器状态为激活', 'log_recommended_action': '无'}]


    elif module == "RDDC":

        if log_type_desc == "RDDC_ACTIVENODE_CHANGE":
            pattern_logs = [{'patterns': [
                'Redundancy group %{DATA:redundancyGroupName} active node changed to %{DATA:activeNodeInformation}, because of %{DATA:statusChangeReason}.'],
                             'log_explanation': '由于用户配置了手工倒换，配置变更或权重变换，冗余组激活节点发生切换', 'log_recommended_action': '无'}]


    elif module == "RESMON":

        if log_type_desc == "RESMON_MINOR":
            pattern_logs = [{'patterns': [
                'Free resource decreased to or below minor threshold %{DATA:minorResourceDepletionThreshold}. %{DATA:resourceUsageDescription}.'],
                             'log_explanation': '当资源剩余值小于或等于低级别告警门限时，资源进入低级别告警状态，并定期输出该日志',
                             'log_recommended_action': '请根据具体的资源类型操作设备，使资源得到合理分配'}]

        elif log_type_desc == "RESMON_MINOR_RECOVER":
            pattern_logs = [{'patterns': [
                'Free resource increased above minor threshold %{DATA:minorResourceDepletionThreshold}. %{DATA:resourceUsageDescription}.'],
                             'log_explanation': '当资源处于低级别告警状态，且剩余值大于低级别告警门限，则资源解除低级别告警状态，并输出该日志。资源使用率进入正常范围',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "RESMON_SEVERE":
            pattern_logs = [{'patterns': [
                'Free resource decreased to or below severe threshold %{DATA:severeResourceDepletionThreshold}. %{DATA:resourceUsageDescription}.'],
                             'log_explanation': '当资源剩余值小于或等于高级别告警门限，且资源没有被使用完，则资源进入高级别告警状态，并定期输出该日志',
                             'log_recommended_action': '请根据具体的资源类型操作设备，使资源得到合理分配'}]

        elif log_type_desc == "RESMON_SEVERE_RECOVER":
            pattern_logs = [{'patterns': [
                'Free resource increased above severe threshold %{DATA:severeResourceDepletionThreshold}. %{DATA:resourceUsageDescription}.'],
                             'log_explanation': '当资源处于高级别告警状态，并且剩余值大于高级别告警门限时，解除高级别告警状态，并输出该日志',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "RESMON_USEDUP":
            pattern_logs = [{'patterns': ['Resources used up. %{DATA:resourceUsageDescription}.'],
                             'log_explanation': '当资源被使用完时，资源进入用完状态，并定期输出该日志',
                             'log_recommended_action': '请尽快清理资源中不用的数据或者表项，以免对应业务受影响'}]

        elif log_type_desc == "RESMON_USEDUP_RECOVER":
            pattern_logs = [{'patterns': [
                'The amount of free resources increased from zero to a non-zero value. %{DATA:additionalResourceUsageInformation}.'],
                             'log_explanation': '当资源处于用完状态，且资源被释放，则解除用完状态，并输出该日志', 'log_recommended_action': '无'}]


    elif module == "RIP":

        if log_type_desc == "RIP_MEM_ALERT":
            pattern_logs = [{'patterns': ['RIP Process received system memory alert %{DATA:typeMemoryAlarm} event.'],
                             'log_explanation': 'RIP模块收到内存告警信息',
                             'log_recommended_action': '当超过各级内存门限时，检查系统内存占用情况，对占用内存较多的模块进行调整，尽量释放可用内存'}]

        elif log_type_desc == "RIP_RT_LMT":
            pattern_logs = [
                {'patterns': ['RIP %{NUMBER:processId:int} Route limit reached'], 'log_explanation': 'RIP进程的路由数达到了上限值',
                 'log_recommended_action': '检查是否受到攻击或者减少网络路由数'}]


    elif module == "RIPNG":

        if log_type_desc == "RIPNG_MEM_ALERT":
            pattern_logs = [{'patterns': ['RIPng Process receivedsystem memory alert %{DATA:typeMemoryAlarm} event.'],
                             'log_explanation': 'RIPng模块收到内存告警信息',
                             'log_recommended_action': '当超过各级内存门限时，检查系统内存占用情况，对占用内存较多的模块进行调整，尽量释放可用内存'}]

        elif log_type_desc == "RIPNG_RT_LMT":
            pattern_logs = [{'patterns': ['RIPng %{NUMBER:processId:int} Route limit reached'],
                             'log_explanation': 'RIPng进程的路由数达到了上限值', 'log_recommended_action': '检查是否受到攻击或者减少网络路由数'}]


    elif module == "RM":

        if log_type_desc == "RM_ACRT_REACH_LIMIT":
            pattern_logs = [{'patterns': [
                'Max active %{DATA:ipv4Ipv6} routes %{NUMBER:maximumNumberActiveRoutes:int} reached in URT of %{DATA:vpnInstanceName}'],
                             'log_explanation': 'VPN实例单播路由表中的激活路由数达到了上限值',
                             'log_recommended_action': '检查所有的路由并删除不需要的路由'}]

        elif log_type_desc == "RM_ACRT_REACH_THRESVALUE":
            pattern_logs = [{'patterns': [
                'Threshold value %{NUMBER:thresholdMaximumNumberActiveRoutesPercentage:int} of max active %{DATA:ipv4Ipv6} routes reached in URT of %{DATA:vpnInstanceName}'],
                             'log_explanation': 'VPN实例单播路由表中的激活路由数达到了最大路由数告警百分比',
                             'log_recommended_action': '修改最大路由数告警百分比或路由数上限值'}]

        elif log_type_desc == "RM_THRESHLD_VALUE_REACH":
            pattern_logs = [{'patterns': [
                'Threshold value %{NUMBER:maximumNumberActiveRoutes:int} of active %{DATA:ipv4Ipv6} routes reached in URT of %{DATA:vpnInstanceName}'],
                             'log_explanation': 'VPN实例单播路由表中的激活路由数达到了上限值', 'log_recommended_action': '修改路由数上限值'}]

        elif log_type_desc == " RM_TOTAL_THRESHLD_VALUE_REACH":
            pattern_logs = [{'patterns': [
                'Threshold value %{NUMBER:maximumNumberActiveRoutes:int} reached for active %{DATA:ipv4Ipv6} routes in all URTs'],
                             'log_explanation': '公网和所有VPN实例的激活路由总数达到了告警值',
                             'log_recommended_action': '检查路由表确认是否需要进行相关处理'}]


    elif module == "RPR":

        if log_type_desc == "RPR_EXCEED_MAX_SEC_MAC":
            pattern_logs = [{'patterns': [
                'A maximum number of secondary MAC addresses exceeded defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上次级MAC地址的数量超过了最大数量',
                             'log_recommended_action': '关闭RPR环上配有VRRP功能站点的VRRP功能'}]

        elif log_type_desc == "RPR_EXCEED_MAX_SEC_MAC_OVER":
            pattern_logs = [{'patterns': [
                'A maximum number of secondary MAC addresses exceeded defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上次级MAC地址的数量不再超过最大数量', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_EXCEED_MAX_STATION":
            pattern_logs = [{'patterns': [
                'A maximum number of stations exceeded defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点的数量超过了最大数量', 'log_recommended_action': '减少RPR环上站点的数量'}]

        elif log_type_desc == "RPR_EXCEED_MAX_STATION_OVER":
            pattern_logs = [{'patterns': [
                'A maximum number of stations exceeded defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点的数量不再超过最大数量', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_EXCEED_RESERVED_RATE":
            pattern_logs = [{'patterns': [
                'An excess reserved rate defect is present on ringlet0/ringlet1 corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点配置的预留带宽总和超过了环路带宽',
                             'log_recommended_action': '减少站点的预留带宽，使其总和不大于环路带宽'}]

        elif log_type_desc == "RPR_EXCEED_RESERVED_RATE_OVER":
            pattern_logs = [{'patterns': [
                'An excess reserved rate defect is cleared on ringlet0/ringlet1 corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点配置的预留带宽总和不再超过环路带宽', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_IP_DUPLICATE":
            pattern_logs = [{'patterns': [
                'A duplicate IP address defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上至少两个站点间的IP地址重复',
                             'log_recommended_action': '找到IP地址相同的站点，并修改其IP地址'}]

        elif log_type_desc == "RPR_IP_DUPLICATE_OVER":
            pattern_logs = [{'patterns': [
                'A duplicate IP address defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点的IP地址不再相同', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_JUMBO_INCONSISTENT":
            pattern_logs = [{'patterns': [
                'A jumbo configuration defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上至少两个站点间的Jumbo帧配置不一致',
                             'log_recommended_action': '找到Jumbo帧配置不一致的站点，并修改其Jumbo帧配置'}]

        elif log_type_desc == "RPR_JUMBO_INCONSISTENT_OVER":
            pattern_logs = [{'patterns': [
                'A jumbo configuration defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点的Jumbo帧配置一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_LAGGCONFIG_INCONSISTENT":
            pattern_logs = [{'patterns': [
                'An inconsistent LAGG configuration is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上，本站点与邻居站点的RPR逻辑接口的聚合配置不一致',
                             'log_recommended_action': '使用display link-aggregation verbose命令检查本站点和邻居站点的RPR逻辑接口的聚合配置，确保本站点和邻居站点上的聚合配置保持一致'},
                            {'patterns': [
                                'An inconsistent LAGG configuration is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上，本站点与邻居站点的RPR逻辑接口的聚合配置已经更改为一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_MISCABLING":
            pattern_logs = [{'patterns': [
                'A miscabling defect is present on ringlet0/ringlet1 corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': '站点的西向/东向边连接到了其它站点的西向/东向边',
                             'log_recommended_action': '检查站点与其它站点间的RPR物理端口是否连接错误'}]

        elif log_type_desc == "RPR_MISCABLING_OVER":
            pattern_logs = [{'patterns': [
                'A miscabling defect is cleared on ringlet0/ringlet1 corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': '站点与其它站点间的RPR物理端口连接正确', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_PROTECTION_INCONSISTENT":
            pattern_logs = [{'patterns': [
                'A protection configuration defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上至少两个站点间的保护模式配置不一致',
                             'log_recommended_action': '找到保护模式配置不一致的站点，并修改其保护模式配置'}]

        elif log_type_desc == "RPR_PROTECTION_INCONSISTENT_OVER":
            pattern_logs = [{'patterns': [
                'A protection configuration defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点的保护模式配置一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_SEC_MAC_DUPLICATE":
            pattern_logs = [{'patterns': [
                'A duplicate secondary MAC addresses defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上至少两个站点间的次级MAC地址重复',
                             'log_recommended_action': '找到次级MAC地址相同的站点，并修改其次级MAC地址'}]

        elif log_type_desc == "RPR_SEC_MAC_DUPLICATE_OVER":
            pattern_logs = [{'patterns': [
                'A duplicate secondary MAC addresses defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环上站点的次级MAC地址不再相同', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_TOPOLOGY_INCONSISTENT":
            pattern_logs = [{'patterns': [
                'An inconsistent topology defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': '站点上不同端口收集的拓扑信息不一致',
                             'log_recommended_action': '在链路上依次执行shutdown和undo shutdown命令，使站点重新收集拓扑信息'}]

        elif log_type_desc == "RPR_TOPOLOGY_INCONSISTENT_OVER":
            pattern_logs = [{'patterns': [
                'An inconsistent topology defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': '站点上不同端口收集的拓扑信息已一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_TOPOLOGY_INSTABILITY":
            pattern_logs = [{'patterns': [
                'A topology instability defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环的拓扑不稳定', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_TOPOLOGY_INSTABILITY_OVER":
            pattern_logs = [{'patterns': [
                'A topology instability defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': 'RPR环的拓扑已稳定', 'log_recommended_action': '无'}]

        elif log_type_desc == "RPR_TOPOLOGY_INVALID":
            pattern_logs = [{'patterns': [
                'A topology invalid defect is present on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': '站点收集的拓扑信息无效',
                             'log_recommended_action': '在链路上依次执行shutdown和undo shutdown命令，使站点重新收集拓扑信息'}]

        elif log_type_desc == "RPR_TOPOLOGY_INVALID_OVER":
            pattern_logs = [{'patterns': [
                'A topology invalid defect is cleared on the ring corresponding to RPR logical interface %{DATA:interfaceName}.'],
                             'log_explanation': '站点收集的拓扑信息有效', 'log_recommended_action': '无'}]


    elif module == "RRPP":

        if log_type_desc == "RRPP_RING_FAIL":
            pattern_logs = [{'patterns': ['Ring %{NUMBER:ringId:int} in Domain %{NUMBER:domainId:int} failed.'],
                             'log_explanation': 'RRPP域下的环链路故障', 'log_recommended_action': '检测RRPP环的各个节点，清除网络故障'}]

        elif log_type_desc == "RRPP_RING_RESTORE":
            pattern_logs = [{'patterns': ['Ring %{NUMBER:ringId:int} in Domain %{NUMBER:domainId:int} recovered.'],
                             'log_explanation': 'RRPP域下的环故障恢复', 'log_recommended_action': '无'}]


    elif module == "RTM":

        if log_type_desc == "RTM_ENVIRONMENT":
            pattern_logs = [{'patterns': ["Can't find environment variable %{DATA:nameEaaEnvironmentVariable}."],
                             'log_explanation': 'CLI监控策略替换环境变量时没有找到对应的环境变量，CLI监控策略执行失败',
                             'log_recommended_action': '请先定义环境变量再使用环境变量'}]

        elif log_type_desc == "RTM_TCL_LOAD_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to load the Tcl script file of policy %{DATA:nameTcl-definedPolicy}.'],
                 'log_explanation': 'Tcl监控策略对应的文件加载到内存失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "RTM_TCL_MODIFY":
            pattern_logs = [{'patterns': [
                "Failed to execute Tcl-defined policy %{DATA:nameTcl-definedPolicy} because the policy's Tcl script file had been modified."],
                             'log_explanation': 'Tcl监控策略触发执行时，对应的文件被修改',
                             'log_recommended_action': '确保Tcl监控策略对应的文件与注册文件相同或者重新创建Tcl监控策略'}]

        elif log_type_desc == "RTM_TCL_NOT_EXIST":
            pattern_logs = [{'patterns': [
                "Failed to execute Tcl-defined policy %{DATA:nameTcl-definedPolicy} because the policy's Tcl script file was not found."],
                             'log_explanation': 'Tcl监控策略触发执行时对应的文件不存在',
                             'log_recommended_action': '确保Tcl监控策略对应的文件存在或者重新创建Tcl监控策略'}]


    elif module == "SCMD":

        if log_type_desc == "PROCESS_ABNORMAL":
            pattern_logs = [{'patterns': [
                'The process %{DATA:processName} exited abnormally. ServiceName=%{DATA:serviceNameDefinedScript}, ExitCode=%{DATA:processExitCode}, KillSignal=%{DATA:signalClosedProcess}, StartTime=%{DATA:timeProcessCreated}, StopTime=%{DATA:timeProcessClosed}.'],
                             'log_explanation': '进程异常退出，输出进程异常退出的相关参数，以便定位',
                             'log_recommended_action': '1.      通常情况下，进程异常退出后，会立即自动重启。可使用display process命令查看进程是否存在。如果进程存在，则进程已恢复\n2.      如果进程未恢复，请搜集以下信息：\n¡  在probe视图下，执行view /var/log/trace.log > trace.log，然后将设备存储目录下的trace.log文件通过FTP或TFTP功能，上传到服务器\n¡  联系工程师，将上述文件，发送给工程师进行分析，并保留现场，以便工程师进行进一步分析定位\n3.      如果进程已恢复，但仍需要定位进程异常退出的原因，请执行第二步\n当使用FTP功能将文件上传到服务器时，请使用binary传输模式'}]

        elif log_type_desc == "PROCESS_ACTIVEFAILED":
            pattern_logs = [{'patterns': [
                'The standby process %{DATA:processName} failed to switch to the active process due to uncompleted synchronization, and was restarted.'],
                             'log_explanation': '备用进程还未完成同步时主进程意外退出，导致备进程倒换成主进程失败。进程重启', 'log_recommended_action': '无'}]

        elif log_type_desc == "PROCESS_CORERECORD":
            pattern_logs = [
                {'patterns': ['Exceptions occurred with process %{DATA:processName}. A core dump file was generated.'],
                 'log_explanation': '进程异常退出产生了core文件。core文件用于记录进程异常退出时的相关信息，以便定位',
                 'log_recommended_action': '1.      请使用display exception context命令搜集进程异常信息，并将该异常信息保存到一个文件中\n2.      通过display exception filepath命令查看core文件目录，并通过FTP或TFTP功能，将core文件和记载了异常信息的文件上传到服务器\n3.      联系工程师，将上述文件，发送给工程师进行分析，并保留现场，以便工程师进一步分析定位\n当使用FTP功能将文件上传到服务器时，请使用binary传输模式'}]

        elif log_type_desc == "SCM_ABNORMAL_REBOOT":
            pattern_logs = [{'patterns': [
                'Failed to restore process %{DATA:processName}. Rebooting %{DATA:chassisNumberSlotNumber}.'],
                             'log_explanation': '进程在设备/slot启动过程中，异常退出，尝试自动重启多次后，仍不能恢复，则自动重启设备/slot',
                             'log_recommended_action': '1.      等单板重启后，使用display process命令查看进程是否恢复\n2.      若多次重启后仍不能恢复，联系工程师解决'}]

        elif log_type_desc == "SCM_ABNORMAL_REBOOTMDC":
            pattern_logs = [{'patterns': [
                'Failed to restore process %{DATA:processName} on %{DATA:objectType} %{NUMBER:idMdcContext:int}. Rebooting %{DATA:objectType} %{NUMBER:idMdcContext:int}.'],
                             'log_explanation': '在主用主控板上的用户MDC的在启动过程中，或者在引擎组中主引擎上的Context启动过程中，进程异常退出，尝试自动重启多次后，仍不能恢复，则重启此MDC或Context。此日志在MDC 1或Context 1中输出',
                             'log_recommended_action': '1.      等单板重启后，使用display process命令查看进程是否恢复\n2.      若多次重启后仍不能恢复，联系工程师解决'}]

        elif log_type_desc == "SCM_ABORT_RESTORE":
            pattern_logs = [{'patterns': ['Failed to restore process %{DATA:processName}. Restoration aborted.'],
                             'log_explanation': '进程在系统运行中异常退出，尝试自动重启多次后，仍不能恢复，系统放弃恢复该进程',
                             'log_recommended_action': '1.      任意视图下执行display process log命令查看进程退出详细信息\n2.      重启异常进程所在单板或MDC，尝试恢复\n3.      提供display process log命令的显示信息，联系工程师解决'}]

        elif log_type_desc == "SCM_INSMOD_ADDON_TOOLONG":
            pattern_logs = [{'patterns': [
                'Failed to finish loading %{DATA:kernelFileName} in %{NUMBER:fileLoadingDuration:int} minutes.'],
                             'log_explanation': '设备启动过程中加载内核文件超时',
                             'log_recommended_action': '1.      重启单板，尝试恢复\n2.      联系工程师解决'}]

        elif log_type_desc == "SCM_KERNEL_INIT_TOOLONG":
            pattern_logs = [{'patterns': [
                'Kernel init in sequence %{DATA:kernelEventPhase} function %{DATA:addressFunctionCorrespondingKernelEvent} is still starting for %{NUMBER:timeDuration:int} minutes.'],
                             'log_explanation': '内核初始化时，某个阶段某函数运行时间过长',
                             'log_recommended_action': '1.      重启单板，尝试恢复\n2.      联系工程师解决'}]

        elif log_type_desc == "SCM_KILL_PROCESS":
            pattern_logs = [{'patterns': [
                'The process %{DATA:param0} was killed because it failed to stop within %{DATA:param1}.',
                'The process %{DATA:param2} on %{DATA:param3} %{NUMBER:param4:int} was killed because it failed to stop within %{DATA:param5}.'],
                             'log_explanation': '某进程超过一定时间没按照指令正常停止，则系统会强制杀掉该进程',
                             'log_recommended_action': '1.      系统/MDC/Context稳定后，使用display process命令查看进程是否恢复\n2.      联系工程师解决'}]

        elif log_type_desc == "SCM_PROCESS_STARTING_TOOLONG":
            pattern_logs = [{'patterns': [
                'The process %{DATA:processName} has not finished starting in %{NUMBER:timeDuration:int} hours.',
                'The process %{DATA:processName} on %{DATA:objectType} %{NUMBER:idMdcContext:int} has not finished starting in %{DATA:timeDuration} hours.'],
                             'log_explanation': '进程长时间未启动完成。可能是因为配置太多导致进程启动慢，也可能是进程异常',
                             'log_recommended_action': '1.      大量配置的情况下，设备启动需要较长时间，如果等待6小时后，仍提示进程未完成启动，则可以认为进程已经异常\n2.      重启单板/MDC/Context，尝试恢复。等单板/MDC/Context重启后，使用display process命令查看进程是否恢复\n3.      联系工程师解决'}]

        elif log_type_desc == "SCM_PROCESS_STILL_STARTING":
            pattern_logs = [{'patterns': [
                'The process %{DATA:processName} is still starting for %{NUMBER:timeDuration:int} minutes.',
                'The process %{DATA:processName} on %{DATA:objectType} %{NUMBER:idMdcContext:int} is still starting for %{DATA:timeDuration} minutes.'],
                             'log_explanation': '某进程一直处于启动状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "SCM_SKIP_PROCESS":
            pattern_logs = [{'patterns': [
                'The process %{DATA:processName} was skipped because it failed to start within 6 hours.',
                'The process %{DATA:processName} on %{DATA:objectType} %{NUMBER:idMdcContext:int} was skipped because it failed to start within 6 hours.'],
                             'log_explanation': '某进程超过6小时未启动完成，系统跳过该进程，继续启动',
                             'log_recommended_action': '1.      重启单板/MDC/Context，尝试恢复。等单板/MDC/Context重启后，使用display process命令查看进程是否恢复\n2.      联系工程师解决'}]


    elif module == "SCRLSP":

        if log_type_desc == "SCRLSP_LABEL_DUPLICATE":
            pattern_logs = [{'patterns': [
                'Incoming label %{NUMBER:incomingLabelValue:int} for static CRLSP %{DATA:staticCrlspName} is duplicate.'],
                             'log_explanation': '静态CRLSP的入标签被静态PW或者静态LSP占用。触发该日志的原因可能有：\n1.      在MPLS已使能的情况下，配置了一条入标签被静态PW或者静态LSP占用的静态CRLSP\n2.      在入标签被静态PW或静态LSP占用的静态CRLSP存在的情况下，使能MPLS',
                             'log_recommended_action': '删除该CRLSP，重新配置一条静态CRLSP，并指定一个新的入标签'}]


    elif module == "SFLOW":

        if log_type_desc == "SFLOW_HARDWARE_ERROR":
            pattern_logs = [{'patterns': [
                'Failed to %{DATA:configurationItem} on interface %{DATA:interfaceName} due to %{DATA:failureReason}.'],
                             'log_explanation': '用户执行的配置不会生效。触发该日志的原因可能有：设备不支持的流采样模式',
                             'log_recommended_action': '改用其它采样模式'}]


    elif module == "SHELL":

        if log_type_desc == "SHELL_CMD":
            pattern_logs = [{'patterns': ['Command is %{DATA:param3}.'], 'log_explanation': '记录设备执行过的命令',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_CMD_CONFIRM":
            pattern_logs = [{'patterns': ['Confirm option of command %{DATA:commandString} is %{DATA:confirmOption}.'],
                             'log_explanation': '记录需要用户确认命令的用户选项操作结果', 'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_CMD_EXECUTEFAIL":
            pattern_logs = [
                {'patterns': ['Command %{DATA:commandString} in view %{DATA:commandView} failed to be executed.'],
                 'log_explanation': '设备后台程序下发的命令执行失败', 'log_recommended_action': '定位命令执行失败的具体原因'}]

        elif log_type_desc == "SHELL_CMD_INPUT":
            pattern_logs = [
                {'patterns': ['Input string for the %{DATA:commandString} command is %{DATA:stringEnteredUser}.'],
                 'log_explanation': '当用户执行命令时，如果需要输入相关信息以进行下一步操作，则输入的字符内容将被记录，并产生日志信息\n例如：\n·          在执行save命令保存配置时，需要用户输入配置文件名和路径，用户输入的该信息将被记录\n·          在执行save命令保存配置时，需要用户输入配置文件名和路径，用户输入CTRL_C取消了保存配置操作，则该信息将被记录\n·          在执行save命令保存配置时，需要用户输入配置文件名和路径，用户输入回车，则该信息将被记录',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_CMD_INPUT_TIMEOUT":
            pattern_logs = [{'patterns': ['Operation timed out: Getting input for the %{DATA:commandString} command.'],
                             'log_explanation': '当用户执行命令时，如果需要输入额外信息确认操作，而用户在一定时间内未输入信息，则产生输入超时的日志信息',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_CMD_INVALID_CHARACTER":
            pattern_logs = [{'patterns': [
                'Execution failed for the %{DATA:commandExecuted} command. Reason: The command contains invalid characters \\(? or \\t\\).'],
                             'log_explanation': '当设备使用文本类型的配置文件下发配置时，例如进行配置恢复或配置回滚时，如果配置文件中的命令行里包含无效字符“?”或“\\t”，则输出此日志',
                             'log_recommended_action': '请用户根据需要，将命令行修改为正确形式，进行手动配置'}]

        elif log_type_desc == "SHELL_CMD_MATCHFAIL":
            pattern_logs = [
                {'patterns': ['Command %{DATA:commandString} in view %{DATA:commandView} failed to be matched.'],
                 'log_explanation': '由于命令输入错误，或者当前模式错误等，造成命令匹配错误', 'log_recommended_action': '定位命令匹配失败的具体原因'}]

        elif log_type_desc == "SHELL_CMDDENY":
            pattern_logs = [
                {'patterns': ['Command=%{DATA:commandString} is denied.'], 'log_explanation': '命令执行失败。用户权限不够',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_CMDFAIL":
            pattern_logs = [{'patterns': ['The %{DATA:commandString} command  failed to restore the configuration.'],
                             'log_explanation': '文本配置恢复操作失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_COMMIT":
            pattern_logs = [{'patterns': ['The configuration has been committed.'], 'log_explanation': '配置提交成功',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_COMMIT_DELAY":
            pattern_logs = [{'patterns': [
                'A configuration rollback will be performed in %{NUMBER:configurationCommitDelayTimer:int} minutes.'],
                             'log_explanation': '用户指定配置提交超时时间成功',
                             'log_recommended_action': '请在超时时间内完成配置并提交，如果不能完成可以再次执行configuration commit delay命令延长时间'}]

        elif log_type_desc == "SHELL_COMMIT_REDELAY":
            pattern_logs = [{'patterns': [
                'The commit delay has been reset, a configuration rollback will be performed in %{NUMBER:configurationCommitDelayTimerReconfigured:int} minutes.'],
                             'log_explanation': '用户在指定的超时时间之内再次配置超时时间，提示已经重置超时时间并显示当前超时时间',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SHELL_COMMIT_ROLLBACK":
            pattern_logs = [{'patterns': [
                'The configuration commit delay is overtime, a configuration rollback will be performed.'],
                             'log_explanation': '达到用户指定的配置提交超时时间后，进行配置回滚',
                             'log_recommended_action': '请停止任何配置操作，即将进行配置回滚'}]

        elif log_type_desc == "SHELL_COMMIT_ROLLBACKDONE":
            pattern_logs = [
                {'patterns': ['The configuration rollback has been performed.'], 'log_explanation': '配置回滚完成',
                 'log_recommended_action': '配置回滚完成，请继续操作'}]

        elif log_type_desc == "SHELL_COMMIT_WILLROLLBACK":
            pattern_logs = [{'patterns': [
                'A configuration rollback will be performed in 1 minute. To retain the configuration you have made after executing the configuration commit delay command, execute the commit command.'],
                             'log_explanation': '用户指定的配置提交超时时间超时前1分钟',
                             'log_recommended_action': '请在超时时间内完成配置并提交，如果不能完成可以再次执行configuration commit delay命令延长时间'}]

        elif log_type_desc == "SHELL_CRITICAL_CMDFAIL":
            pattern_logs = [{'patterns': ['Command=%{DATA:commandString} .'], 'log_explanation': '命令执行失败',
                             'log_recommended_action': '无'}]


    elif module == "WEB":

        if log_type_desc == "LOGIN":
            pattern_logs = [
                {'patterns': ['%{DATA:username} logged in from %{DATA:ipAddressUser}.'], 'log_explanation': '用户登录成功',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "LOGOUT":
            pattern_logs = [
                {'patterns': ['%{DATA:username} logged out from %{DATA:ipAddressUser}.'], 'log_explanation': '用户退出登录',
                 'log_recommended_action': '无'}]

        elif log_type_desc == "LOGIN_FAILED":
            pattern_logs = [{'patterns': ['%{DATA:username} failed to log in from %{DATA:ipAddressUser}.'],
                             'log_explanation': '用户登录失败', 'log_recommended_action': '无'}]


    elif module == "SLSP":

        if log_type_desc == "SLSP_LABEL_DUPLICATE":
            pattern_logs = [{'patterns': [
                'Incoming label %{NUMBER:incomingLabelValue:int} for static LSP %{DATA:staticLspName} is duplicate.'],
                             'log_explanation': '静态LSP的入标签被静态PW或者静态CRLSP占用。触发该日志的原因可能有：\n·          在MPLS已使能的情况下，配置了一条入标签被静态PW或静态CRLSP占用的静态LSP\n·          在入标签被静态PW或静态CRLSP占用的静态LSP存在的情况下，使能MPLS',
                             'log_recommended_action': '删除该LSP，重新配置一条静态LSP，并指定一个新的入标签'}]


    elif module == "SMLK":

        if log_type_desc == "SMLK_DRPORT_CHECK":
            pattern_logs = [{'patterns': [
                "Not all the members in smart link group %{NUMBER:param0:int} are DR ports.\nAn IPP port can't be a member of a smart link group."],
                             'log_explanation': 'Smart Link组成员接口为DR接口与非DR接口或IPP接口，成员接口不生效',
                             'log_recommended_action': '配置Smart Link组成员接口都为DR接口或非DR接口或非IPP接口'}]

        elif log_type_desc == "SMLK_LINK_SWITCH":
            pattern_logs = [{'patterns': [
                'Status of port %{DATA:portName} in smart link group %{NUMBER:smartLinkGroupId:int} changes to active.'],
                             'log_explanation': '另一个成员端口接替故障端口转发流量', 'log_recommended_action': '清除网络故障'}]


    elif module == "SNMP":

        if log_type_desc == "SNMP_ACL_RESTRICTION":
            pattern_logs = [{'patterns': [
                'SNMP %{DATA:snmpCommunity/usm-user/group} from %{DATA:ipAddressNms} is rejected due to ACL restriction.'],
                             'log_explanation': '当SNMP报文因ACL限制被拒绝通过时，打印系统日志',
                             'log_recommended_action': '检查SNMP agent上的ACL配置，及agent是否被攻击'}]

        elif log_type_desc == "SNMP_AUTHENTICATION_FAILURE":
            pattern_logs = [{'patterns': ['Failed to authenticate SNMP message.'],
                             'log_explanation': 'NMS向Agent发起SNMP请求，当认证失败时，Agent记录此日志信息', 'log_recommended_action': '无'}]

        elif log_type_desc == "SNMP_GET":
            pattern_logs = [{'patterns': ['The agent received a message.'],
                             'log_explanation': 'NMS向Agent发送Get请求报文。如果SNMP日志功能开启，SNMP模块将记录Get请求相关信息',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SNMP_INFORM_LOST":
            pattern_logs = [{'patterns': [
                'Inform failed to reach NMS %{DATA:nmsHostAddressPortNumber}: Inform %{DATA:notificationNameOid}%{DATA:variable-bindingFieldNotifications}.'],
                             'log_explanation': '设备给NMS发送Inform报文后，未收到NMS的响应报文，则认为NMS不可达。设备会打印该日志方便用户定位\n当日志携带多个参数导致日志超长时，系统会自动将当前日志拆分为多条日志发送，且添加定位符标识“-PART=xx”，xx表示拆分后生成的日志的序号',
                             'log_recommended_action': '检查设备到NMS是否路由可达'}]

        elif log_type_desc == "SNMP_NOTIFY":
            pattern_logs = [{'patterns': ['Notification %{DATA:param0}%{DATA:param1}.'],
                             'log_explanation': 'Agent发送告警给NMS。如果SNMP告警日志功能开启，Agent将记录SNMP告警信息\n当日志携带多个参数导致日志超长时，系统会自动将当前日志拆分为多条日志发送，且添加定位符标识“-PART=xx”，xx表示拆分后生成的日志的序号',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SNMP_SET":
            pattern_logs = [{'patterns': ['The agent received a message.'],
                             'log_explanation': 'NMS向Agent发送Set请求。如果SNMP日志功能开启，SNMP模块将记录Set操作',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SNMP_USM_NOTINTIMEWINDOW":
            pattern_logs = [
                {'patterns': ['SNMPv3 message is not in the time window.'], 'log_explanation': 'SNMPv3消息不在时间窗',
                 'log_recommended_action': '无'}]


    elif module == "SSHC":

        if log_type_desc == "SSHC_ALGORITHM_MISMATCH":
            pattern_logs = [
                {'patterns': ['The SSH client failed to log in because of %{DATA:typeAlgorithm} algorithm mismatch.'],
                 'log_explanation': '算法不匹配，SSH客户端登录失败', 'log_recommended_action': '修改算法，使SSH客户端和服务器使用相同算法'}]

        elif log_type_desc == "SSHC_AUTH_PASSWORD_FAIL":
            pattern_logs = [{'patterns': [
                'SSH user %{DATA:username} failed to pass password authentication because of invalid username or wrong password.'],
                             'log_explanation': '由于用户名无效或者密码错误导致认证失败', 'log_recommended_action': '检查用户是否存在和密码是否正确'}]

        elif log_type_desc == "SSHC_AUTH_PUBLICKEY_FAIL":
            pattern_logs = [{'patterns': ['SSH user %{DATA:username} failed to pass publickey authentication.'],
                             'log_explanation': 'SSH用户没有通过公钥认证', 'log_recommended_action': '检查服务器上保存的用户公钥与客户端上的公钥是否一致'}]

        elif log_type_desc == "SSHC_CONNECT_FAIL":
            pattern_logs = [{'patterns': [
                'The SSH client failed to connect to SSH server %{IP:ipAddressSshServer} port %{NUMBER:portNumberSshServer:int}.'],
                             'log_explanation': '和SSH服务器建立连接失败',
                             'log_recommended_action': '检查IP地址端口是否正确，SSH服务器端是否开启服务'}]

        elif log_type_desc == "SSHC_DECRYPT_FAIL":
            pattern_logs = [{'patterns': [
                'The SSH client failed to use %{DATA:encryptionAlgorithm} to decrypt the packet received from the SSH server.'],
                             'log_explanation': '来自SSH服务器端的报文解密失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "SSHC_DISCONNECT":
            pattern_logs = [{'patterns': [
                'The SSH client was disconnected from the SSH server because the network was not available.'],
                             'log_explanation': 'SSH客户端与服务器由于网络问题断开连接', 'log_recommended_action': '检查网络'}]

        elif log_type_desc == "SSHC_ENCRYPT_FAIL":
            pattern_logs = [{'patterns': [
                'The SSH client failed to use %{DATA:encryptionAlgorithm} to encrypt the packet sent to the SSH server.'],
                             'log_explanation': '发往SSH服务器的报文加密失败', 'log_recommended_action': '请联系技术支持'}]

        elif log_type_desc == "SSHC_HOST_NAME_ERROR":
            pattern_logs = [
                {'patterns': ['The SSH server host name %{DATA:hostName} is incorrect.'], 'log_explanation': '服务器主机名错误',
                 'log_recommended_action': '检查指定的主机名'}]

        elif log_type_desc == "SSHC_KEY_EXCHANGE_FAIL":
            pattern_logs = [{'patterns': ['The SSH client failed to exchange keys with the SSH server.'],
                             'log_explanation': '在密钥交换过程中出现错误',
                             'log_recommended_action': '检查SSH客户端和服务器端的支持的算法类型是否匹配，如不匹配更改SSH客户端支持的算法'}]

        elif log_type_desc == "SSHC_MAC_ERROR":
            pattern_logs = [{'patterns': [
                'The SSH client received from the SSH server a packet with incorrect message authentication code.'],
                             'log_explanation': 'SSH客户端从服务器收到一个MAC错误的报文', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHC_PUBLICKEY_NOT_EXIST":
            pattern_logs = [{'patterns': ['The public key of the SSH server does not exist.'],
                             'log_explanation': '用户登录过程中指定的服务器端公钥不存在',
                             'log_recommended_action': '通过display public-key peer命令检查服务器端指定公钥是否存在'}]

        elif log_type_desc == "SSHC_VERSION_MISMATCH":
            pattern_logs = [{'patterns': ['The SSH client failed to log in because of version mismatch.'],
                             'log_explanation': '版本不匹配，导致SSH客户端登录失败', 'log_recommended_action': '更改SSH客户端的版本号'}]


    elif module == "SSHS":

        if log_type_desc == "SSHS_CERT_VERIFY_FAIL":
            pattern_logs = [{'patterns': ['Failed to verify the certificate because %{DATA:failureReason}.'],
                             'log_explanation': '证书验证失败', 'log_recommended_action': '检查证书有效性'}]

        elif log_type_desc == "SSH_ACL_DENY":
            pattern_logs = [{'patterns': [
                'The SSH Connection %{IP:ipAddressSshClient}\\(%{DATA:vpnInstanceIpAddressSshClientBelongs}\\) request was denied according to ACL rules.'],
                             'log_explanation': 'SSH ACL规则限制登录IP地址。该日志在SSH服务端检测到非法客户端尝试登录时输出',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_ALGORITHM_MISMATCH":
            pattern_logs = [{'patterns': [
                'SSH client %{DATA:ipAddressSshClient} failed to log in because of %{DATA:typeAlgorithm} algorithm mismatch.'],
                             'log_explanation': '算法不匹配，SSH客户端登录失败', 'log_recommended_action': '修改算法，使SSH客户端和服务器使用相同算法'}]

        elif log_type_desc == "SSHS_AUTH_EXCEED_RETRY_TIMES":
            pattern_logs = [{'patterns': [
                'SSH user %{DATA:userName} \\(IP: %{DATA:ipAddressSshClient}\\) failed to log in, because the number of authentication attempts exceeded the upper limit.'],
                             'log_explanation': 'SSH用户登录失败，认证尝试次数达到了最大值',
                             'log_recommended_action': '请SSH用户确认登录信息，并尝试重新登录'}]

        elif log_type_desc == "SSHS_AUTH_FAIL":
            pattern_logs = [{'patterns': [
                "SSH user %{DATA:username} \\(IP: %{DATA:ipAddressSshClient}\\) didn't pass public key authentication for %{DATA:failureReasons}."],
                             'log_explanation': 'SSH用户没有通过公钥认证', 'log_recommended_action': '请SSH用户重新登录'}]

        elif log_type_desc == "SSHS_AUTH_KBDINT_FAIL":
            pattern_logs = [{'patterns': [
                "SSH user %{DATA:username} \\(IP: %{DATA:ipAddressSshClient}\\) didn't pass keyboard-interactive authentication."],
                             'log_explanation': 'SSH用户没有通过keyboard-interactive认证',
                             'log_recommended_action': '请SSH用户重新登录'}]

        elif log_type_desc == "SSHS_AUTH_PWD_LOG":
            pattern_logs = [{'patterns': [
                'Authentication failed for user %{DATA:username} from %{DATA:ipAddressSshClient} port %{NUMBER:portNumber:int} because of invalid username or wrong password.'],
                             'log_explanation': '由于用户名无效或者密码错误导致认证失败', 'log_recommended_action': '检查用户名密码'}]

        elif log_type_desc == "SSHS_AUTH_SUCCESS":
            pattern_logs = [{'patterns': [
                'SSH user %{DATA:username} from %{IP:ipAddressSshClient} port %{NUMBER:tcpSourcePort:int} passed %{DATA:authenticationMethod} authentication.'],
                             'log_explanation': 'SSH用户认证通过', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_AUTH_TIMEOUT":
            pattern_logs = [{'patterns': ['Authentication timed out for %{IP:ipAddressSshClient}.'],
                             'log_explanation': 'SSH用户认证超时。该日志在SSH服务端检测到用户认证超时时输出',
                             'log_recommended_action': '建议用户检查是否没有及时输入认证信息'}]

        elif log_type_desc == "SSHS_AUTHOR_FAIL":
            pattern_logs = [{'patterns': [
                'Authorization failed for user %{DATA:username} from %{DATA:ipAddressSshClient} port %{NUMBER:portNumber:int}.'],
                             'log_explanation': 'SSH用户授权失败', 'log_recommended_action': '检查本地用户配置或者认证服务器配置'}]

        elif log_type_desc == "SSHS_CONNECT":
            pattern_logs = [{'patterns': [
                'SSH user %{DATA:username} \\(IP: %{DATA:ipAddressSshClient}\\) connected to the server successfully.'],
                             'log_explanation': 'SSH用户成功登录服务器', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_DECRYPT_FAIL":
            pattern_logs = [{'patterns': [
                'The packet from %{DATA:ipAddressSshClient} failed to be decrypted with %{DATA:encryptionAlgorithm}.'],
                             'log_explanation': '来自SSH客户端的报文解密失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_DISCONNECT":
            pattern_logs = [{'patterns': [
                'SSH user %{DATA:username} \\(IP: %{DATA:ipAddressSshClient}\\) disconnected from the server.'],
                             'log_explanation': 'SSH用户退出登录', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_ENCRYPT_FAIL":
            pattern_logs = [{'patterns': [
                'The packet to %{DATA:ipAddressSshClient} failed to be encrypted with %{DATA:encryptionAlgorithm}.'],
                             'log_explanation': '发往SSH客户端的报文加密失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_LOG":
            pattern_logs = [{'patterns': [
                'Authentication failed for user %{DATA:param0} from %{DATA:param1} port %{NUMBER:param2:int} because of invalid username or wrong password.',
                'Authorization failed for user %{DATA:param3} from %{DATA:param4} port %{NUMBER:param5:int}.'],
                             'log_explanation': '由于用户名无效或者密码错误导致认证失败\nSSH用户授权失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_MAC_ERROR":
            pattern_logs = [{'patterns': [
                'SSH server received a packet with wrong message authentication code \\(MAC\\) from %{DATA:ipAddressSshClient}.'],
                             'log_explanation': 'SSH服务器从客户端收到一个MAC错误的报文', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_REACH_SESSION_LIMIT":
            pattern_logs = [{'patterns': [
                'SSH client %{DATA:ipAddressSshClient} failed to log in. The current number of SSH sessions is %{NUMBER:currentNumberSshSessions:int}. The maximum number allowed is %{NUMBER:maximumNumberSshSessionsAllowedDevice:int}.'],
                             'log_explanation': 'SSH客户端登录失败，SSH会话数达到了最大值', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_REACH_USER_LIMIT":
            pattern_logs = [{'patterns': [
                'SSH client %{DATA:ipAddressSshClient} failed to log in, because the number of users reached the upper limit.'],
                             'log_explanation': 'SSH客户端登录失败，SSH用户数达到了最大值', 'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_SFTP_OPER":
            pattern_logs = [{'patterns': [
                'User %{DATA:username} at %{IP:ipAddressSftpClient} requested operation: %{DATA:requestedOperationsFileDirectory}.'],
                             'log_explanation': 'SFTP用户请求相关操作信息。该日志在SFTP服务端收到用户请求执行相关命令时输出',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "SSHS_SRV_UNAVAILABLE":
            pattern_logs = [{'patterns': [
                'The %{DATA:param0} server is disabled or the %{DATA:param1} service type is not supported.'],
                             'log_explanation': 'Stelnet/SCP/SFTP/NETCONF over SSH服务不可用，服务器正在断开连接',
                             'log_recommended_action': '检查服务状态或用户配置'}]

        elif log_type_desc == "SSHS_VERSION_MISMATCH":
            pattern_logs = [
                {'patterns': ['SSH client %{DATA:ipAddressSshClient} failed to log in because of version mismatch.'],
                 'log_explanation': 'SSH客户端和服务器的SSH版本号不匹配', 'log_recommended_action': '修改版本，使SSH客户端和服务器使用相同SSH版本'}]


    elif module == "STP":

        if log_type_desc == "STP_BPDU_PROTECTION":
            pattern_logs = [{'patterns': ['BPDU-Protection port %{DATA:interfaceName} received BPDUs.'],
                             'log_explanation': '使能了BPDU保护功能的接口收到BPDU报文',
                             'log_recommended_action': '检查下行设备是否是用户终端，是否存在恶意攻击'}]

        elif log_type_desc == "STP_BPDU_RECEIVE_EXPIRY":
            pattern_logs = [{'patterns': [
                "Instance %{NUMBER:instanceId:int}'s port %{DATA:interfaceName} received no BPDU within the rcvdInfoWhile interval. Information of the port aged out."],
                             'log_explanation': '非指定端口因在BPDU超时之前没有收到任何BPDU报文，端口状态发生改变',
                             'log_recommended_action': '检查上行设备的STP状态及是否存在恶意攻击'}]

        elif log_type_desc == "STP_CONSISTENCY_CHECK":
            pattern_logs = [{'patterns': [
                'DR role assignment finished. Please verify that the local device and the peer device have consistent global and DR-interface-specific STP settings.'],
                             'log_explanation': '确保分布式聚合系统中两台DR设备上生成树全局和DR口上的配置一致', 'log_recommended_action': '无'}]

        elif log_type_desc == "STP_CONSISTENCY_RESTORATION":
            pattern_logs = [
                {'patterns': ["Consistency restored on VLAN %{NUMBER:vlanId:int}'s port %{DATA:interfaceName}."],
                 'log_explanation': '接口类型不一致或者PVID不一致的保护状态解除', 'log_recommended_action': '无'}]

        elif log_type_desc == "STP_DETECTED_TC":
            pattern_logs = [{'patterns': [
                "%{DATA:instanceVlan} %{NUMBER:instanceIdVlanId:int}'s port %{DATA:interfaceName} detected a topology change."],
                             'log_explanation': '接口所在生成树实例或VLAN拓扑发生变化，本端设备检测到拓扑变化',
                             'log_recommended_action': '检查拓扑变化的原因。如果是有链路down了，就恢复此故障链路'}]

        elif log_type_desc == "STP_DISABLE":
            pattern_logs = [{'patterns': ['STP is now disabled on the device.'], 'log_explanation': '设备全局去使能了生成树特性',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "STP_DISCARDING":
            pattern_logs = [{'patterns': [
                "Instance %{NUMBER:instanceId:int}'s port %{DATA:interfaceName} has been set to discarding state."],
                             'log_explanation': 'MSTP在计算实例内端口状态，该接口被置为discarding状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "STP_DISPUTE":
            pattern_logs = [{'patterns': [
                "%{DATA:instanceVlan} %{NUMBER:instanceIdVlanId:int}'s port %{DATA:interfaceName} received an inferior BPDU from a designated port which is in forwarding or learning state."],
                             'log_explanation': '在生成树实例或VLAN内，端口收到了指定端口发出的低优先级BPDU报文，且发送端口处于Forwarding或Learning状态',
                             'log_recommended_action': '通过display stp abnormal-port命令查看处于Dispute保护的阻塞端口信息。检查链路上是否存在对端接收不到本端所发报文的单通故障。确保两端的端口VLAN配置一致后，可以尝试down/up链路恢复或更换连线'}]

        elif log_type_desc == "STP_ENABLE":
            pattern_logs = [{'patterns': ['STP is now enabled on the device.'], 'log_explanation': '设备全局使能了生成树特性',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "STP_FORWARDING":
            pattern_logs = [{'patterns': [
                "Instance %{NUMBER:instanceId:int}'s port %{DATA:interfaceName} has been set to forwarding state."],
                             'log_explanation': 'STP在计算实例内端口状态，该接口被置为forwarding状态', 'log_recommended_action': '无'}]

        elif log_type_desc == "STP_LOOP_PROTECTION":
            pattern_logs = [{'patterns': [
                "Instance %{NUMBER:instanceId:int}'s LOOP-Protection port %{DATA:interfaceName} failed to receive configuration BPDUs."],
                             'log_explanation': '使能了环路保护功能的接口不能接受BPDU配置报文',
                             'log_recommended_action': '检查上行设备的STP状态及是否存在恶意攻击'}]

        elif log_type_desc == "STP_LOOPBACK_PROTECTION":
            pattern_logs = [{'patterns': [
                "%{DATA:instanceVlan} %{NUMBER:instanceIdVlanId:int}'s port %{DATA:interfaceName} received its own BPDU."],
                             'log_explanation': '在生成树实例或VLAN中，端口收到自己发出的BPDU报文',
                             'log_recommended_action': '检查是否有恶意用户伪造BPDU攻击网络或者网络中是否存在环路'}]

        elif log_type_desc == "STP_NOT_ROOT":
            pattern_logs = [
                {'patterns': ['The current switch is no longer the root of instance %{NUMBER:instanceId:int}.'],
                 'log_explanation': '本设备某生成树实例配置为根桥，但它收到比自身更优的BPDU报文后，就不再是此实例的根桥',
                 'log_recommended_action': '检查桥优先级配置及是否存在恶意攻击'}]

        elif log_type_desc == "STP_NOTIFIED_TC":
            pattern_logs = [{'patterns': [
                "%{DATA:param0} %{NUMBER:param1:int}'s port %{DATA:param2} was notified a topology change."],
                             'log_explanation': '远端相连设备通知本设备某接口所在生成树实例或VLAN的拓扑发生变化',
                             'log_recommended_action': '检查拓扑变化的原因。如果是有链路down了，就恢复此故障链路'}]

        elif log_type_desc == "STP_PORT_TYPE_INCONSISTENCY":
            pattern_logs = [{'patterns': [
                'Access port %{DATA:interfaceName} in VLAN %{NUMBER:vlanId:int} received PVST BPDUs from a trunk or hybrid port.'],
                             'log_explanation': 'Access接口收到了对端Trunk或Hybrid接口发出的PVST报文',
                             'log_recommended_action': '检查两端的接口类型配置是否一致'}]

        elif log_type_desc == "STP_PVID_INCONSISTENCY":
            pattern_logs = [{'patterns': [
                'Port %{DATA:interfaceName} with PVID %{NUMBER:vlanId:int} received PVST BPDUs from a port with PVID %{NUMBER:vlanId:int}.'],
                             'log_explanation': '接口收到了PVID不一致的报文', 'log_recommended_action': '检查两端的接口PVID配置是否一致'}]

        elif log_type_desc == "STP_PVST_BPDU_PROTECTION":
            pattern_logs = [{'patterns': [
                'PVST BPDUs were received on port %{DATA:interfaceName}, which is enabled with PVST BPDU protection.'],
                             'log_explanation': '在MSTP模式下，设备上使能了PVST报文保护功能的端口收到了PVST报文',
                             'log_recommended_action': '检查其他设备是否发出了PVST BPDU'}]

        elif log_type_desc == "STP_ROOT_PROTECTION":
            pattern_logs = [{'patterns': [
                "Instance %{NUMBER:instanceId:int}'s ROOT-Protection port %{DATA:interfaceName} received superior BPDUs."],
                             'log_explanation': '使能了根保护功能的接口收到了比自身BPDU报文更优的BPDU报文',
                             'log_recommended_action': '检查桥优先级配置及是否存在恶意攻击'}]

        elif log_type_desc == "STP_STG_NUM_DETECTION":
            pattern_logs = [{'patterns': [
                "STG count %{NUMBER:numberStgsCard:int} is smaller than the MPU's STG count %{NUMBER:numberStgsMpu:int}."],
                             'log_explanation': '检测到指定单板上的STG个数小于主控板上的STG个数',
                             'log_recommended_action': '配置的STP实例个数不能大于所有单板的STG个数的最小值。例如：配置STP实例数是m，所有单板中，STG个数最小的一块单板的STG数是n，m不能大于n'}]


    elif module == "SYSEVENT":

        if log_type_desc == "EVENT_TIMEOUT":
            pattern_logs = [{'patterns': [
                "Module %{NUMBER:param0:int}'s processing for event %{NUMBER:param1:int} timed out.",
                "Module %{NUMBER:param2:int}'s processing for event %{NUMBER:param3:int} on %{DATA:param4} timed out."],
                             'log_explanation': '应用模块处理事件超时\n非缺省MDC/Context上打印的日志信息不包含MDC MDC-ID或Context Context-ID\n缺省MDC/Context上打印的本MDC/Context的日志信息不包含MDC MDC-ID或Context Context-ID\n缺省MDC/Context上打印的其它MDC/Context的日志信息包含MDC MDC-ID或Context Context-ID',
                             'log_recommended_action': '无'}]


    elif module == "SYSLOG":

        if log_type_desc == "SYSLOG_LOGBUFFER_FAILURE":
            pattern_logs = [{'patterns': [
                'Log cannot be sent to the logbuffer because of communication timeout between syslog and DBM processes.'],
                             'log_explanation': '日志无法输出到日志缓冲区，因为Syslog进程和DBM进程通信超时',
                             'log_recommended_action': '请重启设备或者联系技术支持人员'}]

        elif log_type_desc == "SYSLOG_LOGFILE_FULL":
            pattern_logs = [{'patterns': ['Log file space is full.'], 'log_explanation': '日志空间已满',
                             'log_recommended_action': '备份日志文件后将其删除，然后根据需要使能端口'}]

        elif log_type_desc == "SYSLOG_NO_SPACE":
            pattern_logs = [{'patterns': ['Failed to save log file due to lack of space resources.'],
                             'log_explanation': '存储介质空间不足，将日志保存到日志文件失败',
                             'log_recommended_action': '请定期清理存储介质的存储空间，以免影响日志文件功能'}]

        elif log_type_desc == "SYSLOG_RESTART":
            pattern_logs = [{'patterns': ['System restarted --\n%{DATA:companyName} %{DATA:softwareName} Software.'],
                             'log_explanation': '系统重启日志', 'log_recommended_action': '无'}]

        elif log_type_desc == "SYSLOG_RTM_EVENT_BUFFER_FULL":
            pattern_logs = [{'patterns': [
                'In the last minute, %{DATA:numberSystemLogsSentEaaModuleLastMinute} syslog logs were not monitored because the buffer was full.'],
                             'log_explanation': '设备在短时间内产生大量日志，导致EAA监控的日志缓冲区被占满，有多条日志没来得及匹配便被丢弃了',
                             'log_recommended_action': '·          找到日志的来源，减少日志的生成\n·          使用rtm event syslog buffer-size命令增大EAA监控的日志缓冲区的大小'}]


    elif module == "TCSM":

        if log_type_desc == "TCSM_CERT_BROKEN":
            pattern_logs = [{'patterns': ['Certificate %{DATA:certificateName} is missing or corrupted.'],
                             'log_explanation': '保存在存储介质中的证书文件已丢失或损坏',
                             'log_recommended_action': '1.      建议更换存储介质\n2.      通过管理端为设备的TCSM密钥重新签发证书\n3.      如果丢失/损坏的是系统预置证书（以default为前缀的证书），请联系技术支持'}]

        elif log_type_desc == "TCSM_KEY_BROKEN":
            pattern_logs = [
                {'patterns': ['Key %{DATA:keyName} is corrupted or missing.'], 'log_explanation': '保存在存储介质中的密钥文件已丢失或损坏',
                 'log_recommended_action': '1.      如果该密钥还存在，删除该密钥（相关命令为key destroy）\n2.      建议更换存储介质\n3.      如果丢失/损坏的是系统预置密钥，请联系技术支持'}]

        elif log_type_desc == "TCSM_KEY_HIERARCHY_BROKEN":
            pattern_logs = [
                {'patterns': ['Key hierarchy of %{DATA:keyName} is corrupted.'], 'log_explanation': '指定密钥的上层密钥已损坏',
                 'log_recommended_action': '1.      删除该密钥及其上层密钥（相关命令为key destroy）\n2.      建议更换存储介质'}]

        elif log_type_desc == "TCSM_TSS_SVC_DOWN":
            pattern_logs = [{'patterns': ['TSS service is down.'], 'log_explanation': 'TSS进程down',
                             'log_recommended_action': '请联系技术支持'},
                            {'patterns': ['TSS service is up.'], 'log_explanation': 'TSS进程up',
                             'log_recommended_action': '无'}]


    elif module == "TELNETD":

        if log_type_desc == "TELNETD_ACL_DENY":
            pattern_logs = [{'patterns': [
                'The Telnet Connection %{IP:ipAddressTelnetClient}\\(%{DATA:vpnInstanceIpAddressTelnetClientBelongs}\\) request was denied according to ACL rules.'],
                             'log_explanation': 'Telnet ACL规则限制登录IP地址。该日志在Telnet服务端检测到非法客户端尝试登录时输出',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "TELNETD_REACH_SESSION_LIMIT":
            pattern_logs = [{'patterns': [
                'Telnet client %{DATA:ipAddressTelnetClient} failed to log in. The current number of Telnet sessions is %{NUMBER:currentNumberTelnetSessions:int}. The maximum number allowed is \\(%{NUMBER:maximumNumberTelnetSessionsAllowedDevice:int}\\).'],
                             'log_explanation': 'Telnet登录用户达到上限。该日志在Telnet服务端检测到登录客户端数达到上限时输出',
                             'log_recommended_action': '请根据需要使用命令aaa session-limit配置允许的Telnet最大登录用户数'}]


    elif module == "TRILL":

        if log_type_desc == "TRILL_DUP_SYSTEMID":
            pattern_logs = [{'patterns': [
                'Duplicate System ID %{DATA:param0} in %{DATA:param1} PDU sourced from RBridge 0x%{DATA:param2}.'],
                             'log_explanation': '本地RBridge收到的LSP或者IIH PDU中的System ID和本地RBridge的System ID相同。可能的原因包括：\n·          为本地RBridge和远端RBridge分配了相同的System ID\n·          本地RBridge收到了一个自己产生、携带了旧的Nickname的LSP PDU',
                             'log_recommended_action': '检查TRILL网络中上RBridge的System ID'}]

        elif log_type_desc == "TRILL_INTF_CAPABILITY":
            pattern_logs = [{'patterns': ['The interface %{DATA:interfaceName} does not support TRILL.'],
                             'log_explanation': '不支持TRILL的端口被加入到了聚合组中',
                             'log_recommended_action': '将不支持TRILL的端口从聚合组中删除'}]

        elif log_type_desc == "TRILL_LICENSE_EXPIRED":
            pattern_logs = [{'patterns': ['The TRILL feature is being disabled, because its license has expired.'],
                             'log_explanation': 'TRILL的License已经过期', 'log_recommended_action': '请更换有效的License'}]

        elif log_type_desc == "TRILL_LICENSE_EXPIRED_TIME":
            pattern_logs = [
                {'patterns': ['The TRILL feature will be disabled in %{NUMBER:availablePeriodFeature:int} days.'],
                 'log_explanation': 'TRILL的License不可用，TRILL功能将在2天后失效\n\n主备倒换后新的主控板上没有可用的TRILL License，会启动30天临时可用定时器',
                 'log_recommended_action': '若要继续使用TRILL功能，请准备新的License'}]

        elif log_type_desc == "TRILL_LICENSE_UNAVAILABLE":
            pattern_logs = [{'patterns': ['The TRILL feature has no available license.'],
                             'log_explanation': '进程启动时，没有找到TRILL对应的License',
                             'log_recommended_action': '请为TRILL安装有效的License'}]

        elif log_type_desc == "TRILL_MEM_ALERT":
            pattern_logs = [
                {'patterns': ['TRILL process receive system memory alert %{DATA:typeMemoryAlertEvent} event.'],
                 'log_explanation': 'TRILL从系统收到一个内存告警事件', 'log_recommended_action': '检查系统内存'}]

        elif log_type_desc == "TRILL_NBR_CHG":
            pattern_logs = [{'patterns': [
                'TRILL %{NUMBER:trillProcessId:int}, %{DATA:neighborLevel} adjacency %{DATA:neighborSystemId} \\(%{DATA:interfaceName}\\), state changed to %{DATA:currentNeighborState}.'],
                             'log_explanation': '一个TRILL邻居的状态发生改变',
                             'log_recommended_action': '当邻居状态变为down或者initializing时，请根据状态变化的原因检查TRILL配置和网络状态'}]


    elif module == "VCF":

        if log_type_desc == "VCF_AGGR_CREAT":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} created Layer 2 aggregation group %{NUMBER:idLayer2AggregationGroup:int}: member ports=%{DATA:listLayer2AggregationMemberPorts}.'],
                             'log_explanation': '创建二层聚合组，并将端口加入对应的聚合组', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_AGGR_DELETE":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} deleted Layer 2 aggregation group %{NUMBER:idLayer2AggregationGroup:int}.'],
                             'log_explanation': '二层聚合组中仅包含一条Up状态的链路时，删除聚合组', 'log_recommended_action': '无'}]

        elif log_type_desc == " VCF_AGGR_FAILED":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} failed to create Layer 2 aggregation group %{NUMBER:idLayer2AggregationGroup:int}.'],
                             'log_explanation': '创建聚合组失败', 'log_recommended_action': '请管理员排查是否因为资源不足等原因造成聚合组创建失败'}]

        elif log_type_desc == "VCF_AUTO_ANALYZE_USERDEF":
            pattern_logs = [
                {'patterns': ['Phase %{DATA:phase}, Device %{DATA:macAddressDevice} started to parse template file.'],
                 'log_explanation': '开始解析模板文件中的用户自定义配置', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_AUTO_NO_USERDEF":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} found undefined variable %{DATA:undefinedUserVariable} in command %{DATA:commandUndefinedUserVariableResides} on line %{NUMBER:numberCommandLine:int}.'],
                             'log_explanation': '解析模板文件过程中，若模板文件中存在无法识别的用户定义变量时，输出此日志信息，提示未找到用户定义的变量。若存在多个无法识别的用户定义变量，则打印多条此日志信息',
                             'log_recommended_action': '需管理员确认模板文件中定义的变量是否正确，修改后重新部署'}]

        elif log_type_desc == "VCF_AUTO_START":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} \\(Role %{DATA:roleDevice}\\) started VCF automated deployment.'],
                             'log_explanation': '自动化部署开始', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_AUTO_STATIC_CMD":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} automatically executed static commands.'],
                             'log_explanation': '执行模板中的静态配置命令，静态配置命令是指与VCF拓扑等动态信息无关的配置命令',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_BGP":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:param0}, Device %{DATA:param1} established a BGP session with peer %{DATA:param2} in AS %{NUMBER:param3:int}.',
                'Phase %{DATA:param4}, Device %{DATA:param5} established a BGP session with peers [%{DATA:param6}] in AS %{NUMBER:param7:int}.'],
                             'log_explanation': 'VCF成功与对等体建立BGP会话\n在三层组网中，仅主Spine节点上会记录该日志信息',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_DOWN_LINK":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} discovered downlink interface %{DATA:nameDownlinkInterface}.'],
                             'log_explanation': 'VCF发现下行接口（Spine设备上连接Leaf的接口或leaf设备连接下游接入设备的接口），并下发配置',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_DRIVER_INIT":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, failed to find driver %{DATA:driverName}. Driver initialization failed.'],
                             'log_explanation': '设备驱动不存在时，提示驱动初始化失败。',
                             'log_recommended_action': '请检查模板对应驱动名称是否正确，联系开发人员确认VCF是否支持该驱动'}]

        elif log_type_desc == "VCF_GET_IMAGE":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} obtained information about update startup image file %{DATA:nameNewStartupImageFile}: new version=%{DATA:versionNumberNewStartupImageFile}, current version=%{DATA:versionNumberCurrentStartupImageFile}.'],
                             'log_explanation': '通过模板文件获取新版本的文件名和版本号', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_GET_TEMPLATE":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} downloaded template file %{DATA:nameTemplateFile}.'],
                             'log_explanation': '将自动部署的模板文件下载到本地设备', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_INSTALL_IMAGE":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} started to install the %{DATA:versionNumberNewStartupImageFile} version of startup image.'],
                             'log_explanation': '设备开始安装新版本', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_IRF_FINISH":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} finished IRF configuration: result=%{NUMBER:resultIrfConfiguration:int}.'],
                             'log_explanation': '完成IRF配置下发', 'log_recommended_action': '如果配置下发失败，请联系用服工程师解决'}]

        elif log_type_desc == "VCF_IRF_FOUND":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} \\(Role %{DATA:roleDevice}\\) found a peer \\(%{DATA:macAddressPeerDevice}\\) with the same role, IRF stackability check result: %{NUMBER:resultIrfStackabilityCheck:int}.'],
                             'log_explanation': 'VCF通过拓扑变化发现对端需要搭建IRF的设备，检查是否能够开始进行IRF配置',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_IRF_START":
            pattern_logs = [{'patterns': [
                "Phase %{DATA:phase}, Device %{DATA:macAddressDevice} started IRF configuration: current member ID=%{NUMBER:currentIrfMemberIdDevice:int}, new member ID=%{NUMBER:newIrfMemberIdDevice:int}, priority=%{NUMBER:newIrfMemberPriorityDevice:int}, IRF-port 1's member ports=%{DATA:listIrfPhysicalInterfacesBoundIrf-port1}, IRF-port 2's member ports=%{DATA:listIrfPhysicalInterfacesBoundIrf-port2}."],
                             'log_explanation': '开始下发IRF配置', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_LOOPBACK_START":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, IP address assignment started for %{DATA:interfaceName} on other nodes.'],
                             'log_explanation': 'VCF主节点开始为其他节点的接口分配IP地址', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_LOOPBACK_START_FAILED":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, failed to assign IP addresses to %{DATA:interfaceName} on other nodes: reason=%{DATA:reasonFailureStartIpAddressAssignment}.'],
                             'log_explanation': 'VCF Fabric组网中，由于以下原因之一，主节点没能开始为其他节点的接口分配IP地址：\n·          没有指定IP范围\n·          IP地址无效',
                             'log_recommended_action': '管理员检查模板中IP范围是否有问题'}]

        elif log_type_desc == "VCF_LOOPBACK_ALLOC":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, assigned IP %{DATA:ipAddress} to %{DATA:interfaceName} on Device %{DATA:macAddressDevice}: result=%{NUMBER:resultIpAddressAssignment:int}.'],
                             'log_explanation': 'VCF主节点为指定设备的接口分配IP地址', 'log_recommended_action': '管理员根据结果查找失败原因'}]

        elif log_type_desc == "VCF_LOOPBACK_NO_FREE_IP":
            pattern_logs = [
                {'patterns': ['Phase %{DATA:phase}, no IP addresses available for Device %{DATA:macAddressDevice}.'],
                 'log_explanation': 'VCF主节点上没有可用的IP地址，无法为指定设备的接口分配IP地址', 'log_recommended_action': '请用户确认IP预留范围是否准确'}]

        elif log_type_desc == "VCF_LOOPBACK_RECLAIM":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, reclaimed IP %{DATA:reclaimedIpAddress} from %{DATA:interfaceName} on Device %{DATA:macAddressDeviceIpAddressReclaimed}: reason=%{NUMBER:reasonReclaimingIpAddress:int}.'],
                             'log_explanation': 'VCF收回已经分配出去的接口的IP地址', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_REBOOT":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} will reboot. Reason: %{DATA:rebootCause}.'],
                             'log_explanation': '完成新版本升级、IRF成员编号变更等操作后，设备自动重启', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_SKIP_INSTALL":
            pattern_logs = [
                {'patterns': ['Phase %{DATA:phase}, Device %{DATA:macAddressDevice} skipped automatic version update.'],
                 'log_explanation': '设备当前运版本与通过模板文件获取的版本一致时，跳过自动更新版本', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_STATIC_CMD_ERROR":
            pattern_logs = [{'patterns': [
                "Phase %{DATA:phase}, Device %{DATA:macAddressDevice} failed to automatically execute static command '%{DATA:commandFailExecuted}' in context '%{DATA:contextCommandResides}'."],
                             'log_explanation': '自动部署过程中执行失败的静态命令', 'log_recommended_action': '管理员查找错误原因，修改错误后需要重新部署'}]

        elif log_type_desc == "VCF_UP_LINK":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} discovered uplink interface %{DATA:nameUplinkInterface}.'],
                             'log_explanation': 'VCF发现上行接口（Leaf设备上连接Spine的接口），并下发配置', 'log_recommended_action': '无'}]

        elif log_type_desc == "VCF_WHITE_LIST_CHECK":
            pattern_logs = [{'patterns': [
                'Phase %{DATA:phase}, Device %{DATA:macAddressDevice} failed whitelist check and automated undelay network deployment stopped.'],
                             'log_explanation': 'VCF模块提示白名单检查失败，Underlay自动化配置下发停止。', 'log_recommended_action': '无'}]


    elif module == "VLAN":

        if log_type_desc == " VLAN_CREATEFAIL":
            pattern_logs = [
                {'patterns': ['Failed to create VLAN %{DATA:vlanId}. The maximum number of VLANs has been reached.'],
                 'log_explanation': '因为VLAN硬件资源不足，导致创建VLAN失败', 'log_recommended_action': '无'}]

        elif log_type_desc == "VLAN_FAILED":
            pattern_logs = [{'patterns': ['Failed to add interface %{DATA:interfaceName} to the default VLAN.'],
                             'log_explanation': '在硬件资源不足的时候创建一个S-Channel接口，此S-Channel接口不能加入到缺省VLAN',
                             'log_recommended_action': '无'}]

        elif log_type_desc == "VLAN_QINQETHTYPE_FAILED":
            pattern_logs = [{'patterns': [
                'Failed to set the TPID value in CVLAN tags to %{NUMBER:tpidValueInnerVlanTags:int} \\(hexadecimal\\). The operation is not supported.'],
                             'log_explanation': '在IRF3.1组网环境中，CB支持配置内层VLAN Tag的TPID值但PEX不支持的情况下，在CB上执行qinq ethernet-type customer-tag命令后打印，提示配置未成功',
                             'log_recommended_action': '确认组网中的PEX设备是否支持配置内层VLAN Tag的TPID值'}]

        elif log_type_desc == "VLAN_VLANTRANSPARENT_FAILED":
            pattern_logs = [{'patterns': [
                'The configuration failed because of resource insufficiency or conflicts on %{DATA:interfaceName}.'],
                             'log_explanation': '因本接口硬件资源不足或者接口加入或离开二层聚合组，所以部分或全部VLAN透传配置丢失',
                             'log_recommended_action': '无'}]


    elif module == "VRRP":

        if log_type_desc == "VRRP_STATUS_CHANGE":
            pattern_logs = [{'patterns': [
                'The status of %{DATA:vrrpVersion} virtual router %{NUMBER:vrrpGroupNumber:int} \\(configured on %{DATA:nameInterfaceVrrpGroupConfigured}\\) changed from %{DATA:originalStatus} to %{DATA:currentStatus}: %{DATA:reasonStatusChange}.'],
                             'log_explanation': 'VRRP备份组中的Master或Backup路由器状态发生变化。可能的原因包括：收到接口事件、虚地址删除、Track对象状态变化、收到VRRP报文、当前设备成为地址拥有者、Master down定时器超时、收到0优先级的报文、发生了抢占或者管理备份组驱动',
                             'log_recommended_action': '检查VRRP备份组中的Master或Backup路由器状态，确保备份组工作正常'}]

        elif log_type_desc == "VRRP_VF_STATUS_CHANGE":
            pattern_logs = [{'patterns': [
                'The %{DATA:vrrpVersion} virtual router %{NUMBER:vrrpGroupNumber:int} \\(configured on %{DATA:nameInterfaceVrrpGroupConfigured}\\) virtual forwarder %{NUMBER:vfId:int} detected status change \\(from %{DATA:originalStatusVf} to %{DATA:currentStatusVf}\\): %{DATA:reasonStatusChange}.'],
                             'log_explanation': '虚拟转发器状态发生改变。可能的原因包括权重变化、定时器超时、VRRP备份组Down',
                             'log_recommended_action': '检查Track项的状态'}]

        elif log_type_desc == "VRRP_VMAC_INEFFECTIVE":
            pattern_logs = [{'patterns': [
                'The %{DATA:vrrpVersion} virtual router %{NUMBER:vrrpGroupNumber:int} \\(configured on %{DATA:nameInterfaceVrrpGroupConfigured}\\) failed to add virtual MAC: %{DATA:reasonError}.'],
                             'log_explanation': '添加虚拟MAC地址失败', 'log_recommended_action': '确定操作失败的根因并解决'}]


    elif module == "VSRP":

        if log_type_desc == "VSRP_BIND_FAILED":
            pattern_logs = [
                {'patterns': ['Failed to bind the IP addresses and the port on VSRP peer %{DATA:vsrpPeerName}.'],
                 'log_explanation': 'TCP端口正在被使用，创建到VSRP对端的TCP连接时接口绑定IP地址失败', 'log_recommended_action': '无'}]


    elif module == "VXLAN":

        if log_type_desc == "VXLAN_LICENSE_UNAVAILABLE":
            pattern_logs = [{'patterns': ['The VXLAN feature is disabled, because no licenses are valid.'],
                             'log_explanation': '因为没有有效的License，VXLAN特性被禁用',
                             'log_recommended_action': '检查VXLAN的License，若要使用VXLAN特性，请安装有效的License'}]


    elif module == "WIPS":

        if log_type_desc == "APFLOOD":
            pattern_logs = [{'patterns': ['AP flood detected.'], 'log_explanation': '指定VSD内检测到AP设备数量过多时触发日志',
                             'log_recommended_action': '检查是否存在攻击'}]

        elif log_type_desc == "AP_CHANNEL_CHANGE":
            pattern_logs = [{'patterns': ['Channel change detected.'], 'log_explanation': '指定VSD内检测到指定AP信道改变时触发日志',
                             'log_recommended_action': '检查AP信道改变是否正常'}]

        elif log_type_desc == "ASSOCIATEOVERFLOW":
            pattern_logs = [{'patterns': ['Association/Reassociation DoS attack detected.'],
                             'log_explanation': '指定VSD内检测到指定AP回应status code为17的关联回应帧时触发日志',
                             'log_recommended_action': '检查AP是否受到攻击'}]

        elif log_type_desc == "HONEYPOT":
            pattern_logs = [{'patterns': ['Honeypot AP detected.'], 'log_explanation': '指定VSD内检测到指定AP为蜜罐时触发日志',
                             'log_recommended_action': '检查是否存在攻击'}]

        elif log_type_desc == "HTGREENMODE":
            pattern_logs = [{'patterns': ['HT-Greenfield AP detected.'], 'log_explanation': '指定VSD内检测到指定AP携带绿野模式时触发日志',
                             'log_recommended_action': '检查是否受到攻击'}]

        elif log_type_desc == "MAN_IN_MIDDLE":
            pattern_logs = [
                {'patterns': ['Man-in-the-middle attack detected.'], 'log_explanation': '指定VSD内检测到指定client受到中间人攻击时触发日志',
                 'log_recommended_action': '检查client是否受到中间人攻击'}]

        elif log_type_desc == "WIPS_DOS":
            pattern_logs = [{'patterns': ['%{DATA:deviceType} rate attack detected.'],
                             'log_explanation': '设备指定VSD内的表项建立速率超过阈值时触发日志', 'log_recommended_action': '检查设备是否受到攻击'}]

        elif log_type_desc == "WIPS_FLOOD":
            pattern_logs = [{'patterns': ['%{DATA:floodAttackType} flood detected.'],
                             'log_explanation': '一定时间内在指定VSD内检测到同一类型的报文超过阈值时触发日志',
                             'log_recommended_action': '检查报文发送者的合法性'}]

        elif log_type_desc == "WIPS_MALF":
            pattern_logs = [{'patterns': ['Error detected: %{DATA:malformedPacketType}.'],
                             'log_explanation': '指定VSD内检测到指定类型的畸形报文时触发日志', 'log_recommended_action': '检查报文发送者的合法性'}]

        elif log_type_desc == "WIPS_SPOOF":
            pattern_logs = [
                {'patterns': ['%{DATA:spoofingAttackType} detected.'], 'log_explanation': '指定VSD内检测到设备仿冒时触发日志',
                 'log_recommended_action': '检查报文发送者的合法性'}]

        elif log_type_desc == "WIPS_WEAKIV":
            pattern_logs = [{'patterns': ['Weak IV detected.'], 'log_explanation': '指定VSD内检测到采用weak IV加密的报文',
                             'log_recommended_action': '使用安全级别更高的加密方法加密报文'}]

        elif log_type_desc == "WIRELESSBRIDGE":
            pattern_logs = [
                {'patterns': ['Wireless bridge detected.'], 'log_explanation': '指定VSD内检测到AP1和AP2建立无线网桥时触发日志',
                 'log_recommended_action': '检查无线网桥是否合法'}]

    return pattern_logs

