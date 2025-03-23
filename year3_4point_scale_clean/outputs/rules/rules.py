def findDecision(obj): #obj[0]: Kỹ năng mềm, obj[1]: Đại số tuyến tính, obj[2]: Giải tích 1, obj[3]: Tin học đại cương, obj[4]: Vật lý điện từ, obj[5]: Giải tích 2, obj[6]: Lập trình nâng cao, obj[7]: Môn tự chọn 1, obj[8]: Thiết kế Web, obj[9]: Toán rời rạc, obj[10]: Cấu trúc dữ liệu và giải thuật, obj[11]: Kiến trúc và tổ chức máy tính, obj[12]: Lập trình hướng đối tượng, obj[13]: Xác suất thống kê, obj[14]: Hệ điều hành, obj[15]: Công nghệ Java, obj[16]: Cơ sở dữ liệu, obj[17]: Phân tích thiết kế thuật toán, obj[18]: Môn tự chọn 2, obj[19]: Lập trình trực quan, obj[20]: Mạng máy tính, obj[21]: Phân tích thiết kế hệ thống, obj[22]: Môn tự chọn 3, obj[23]: Môn tự chọn 4, obj[24]: Môn tự chọn 5, obj[25]: Lập trình Web, obj[26]: Môn tự chọn 6, obj[27]: Môn tự chọn 7, obj[28]: An toàn và bảo mật thông tin, obj[29]: Thực tập chuyên môn , obj[30]: Môn tự chọn 8
	# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 8", "instances": 614, "metric_value": 1.8524, "depth": 1}
	if obj[30] == 'B':
		# {"feature": "C\u01a1 s\u1edf d\u1eef li\u1ec7u", "instances": 263, "metric_value": 1.8234, "depth": 2}
		if obj[16] == 'B':
			# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 116, "metric_value": 1.5793, "depth": 3}
			if obj[11] == 'B':
				# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 36, "metric_value": 1.254, "depth": 4}
				if obj[9] == 'C':
					# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf h\u1ec7 th\u1ed1ng", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[21] == 'C':
						return 'Khá'
					elif obj[21] == 'B':
						return 'Khá'
					else: return 'Khá'
				elif obj[9] == 'B':
					# {"feature": "M\u1ea1ng m\u00e1y t\u00ednh", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[20] == 'B':
						return 'Khá'
					elif obj[20] == 'A':
						return 'Giỏi'
					elif obj[20] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[9] == 'A':
					return 'Giỏi'
				elif obj[9] == 'D':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[11] == 'C':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 33, "metric_value": 1.4014, "depth": 4}
				if obj[4] == 'B':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 13, "metric_value": 1.2389, "depth": 5}
					if obj[10] == 'C':
						return 'Khá'
					elif obj[10] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[10] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[4] == 'A':
					# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 12, "metric_value": 1.2807, "depth": 5}
					if obj[6] == 'A':
						return 'Giỏi'
					elif obj[6] == 'D':
						return 'Giỏi'
					elif obj[6] == 'B':
						return 'Khá'
					elif obj[6] == 'C':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[4] == 'C':
					return 'Khá'
				elif obj[4] == 'D':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[11] == 'D':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 3", "instances": 30, "metric_value": 1.0746, "depth": 4}
				if obj[22] == 'C':
					# {"feature": "L\u1eadp tr\u00ecnh tr\u1ef1c quan", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[19] == 'B':
						return 'Khá'
					elif obj[19] == 'A':
						return 'Khá'
					elif obj[19] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[19] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[22] == 'B':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[4] == 'A':
						return 'Khá'
					elif obj[4] == 'C':
						return 'Khá'
					elif obj[4] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[22] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[22] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Giỏi'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[11] == 'A':
				# {"feature": "L\u1eadp tr\u00ecnh tr\u1ef1c quan", "instances": 17, "metric_value": 1.4517, "depth": 4}
				if obj[19] == 'A':
					# {"feature": "Th\u1ef1c t\u1eadp chuy\u00ean m\u00f4n ", "instances": 14, "metric_value": 1.0949, "depth": 5}
					if obj[29] == 'A':
						return 'Giỏi'
					elif obj[29] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[19] == 'B':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'B':
						return 'Giỏi'
					elif obj[0] == 'C':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[19] == 'D':
					return 'Khá'
				else: return 'Giỏi'
			else: return 'Khá'
		elif obj[16] == 'C':
			# {"feature": "L\u1eadp tr\u00ecnh Web", "instances": 69, "metric_value": 1.3675, "depth": 3}
			if obj[25] == 'D':
				# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 28, "metric_value": 1.5715, "depth": 4}
				if obj[9] == 'C':
					# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 12, "metric_value": 1.4591, "depth": 5}
					if obj[6] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[6] == 'C':
						return 'Khá'
					elif obj[6] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[6] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[9] == 'D':
					# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 5", "instances": 7, "metric_value": 1.3788, "depth": 5}
					if obj[24] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[24] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[9] == 'B':
					# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11] == 'C':
						return 'Khá'
					elif obj[11] == 'D':
						return 'Khá'
					elif obj[11] == 'B':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[9] == 'A':
					return 'Khá'
				else: return 'Khá'
			elif obj[25] == 'C':
				# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 25, "metric_value": 0.795, "depth": 4}
				if obj[8] == 'C':
					# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 5", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[24] == 'B':
						return 'Khá'
					elif obj[24] == 'A':
						return 'Khá'
					elif obj[24] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[8] == 'B':
					# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[12] == 'B':
						return 'Khá'
					elif obj[12] == 'C':
						return 'Khá'
					elif obj[12] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[8] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[8] == '0.3':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[25] == 'B':
				# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[12] == 'A':
					return 'Giỏi'
				elif obj[12] == 'B':
					return 'Khá'
				elif obj[12] == 'C':
					return 'Khá'
				else: return 'Khá'
			elif obj[25] == 'A':
				return 'Khá'
			elif obj[25] == 'F':
				return 'Chưa Xếp Loại'
			elif obj[25] == '0':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[16] == 'A':
			# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 2", "instances": 48, "metric_value": 1.5503, "depth": 3}
			if obj[18] == 'A':
				# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 31, "metric_value": 1.181, "depth": 4}
				if obj[9] == 'A':
					# {"feature": "C\u1ea5u tr\u00fac d\u1eef li\u1ec7u v\u00e0 gi\u1ea3i thu\u1eadt", "instances": 15, "metric_value": 1.2729, "depth": 5}
					if obj[10] == 'B':
						return 'Xuất sắc'
					elif obj[10] == 'C':
						return 'Giỏi'
					elif obj[10] == 'A':
						return 'Xuất sắc'
					elif obj[10] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Xuất sắc'
				elif obj[9] == 'B':
					# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 1", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[7] == 'B':
						return 'Giỏi'
					elif obj[7] == 'A':
						return 'Xuất sắc'
					elif obj[7] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[9] == 'C':
					# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[12] == 'A':
						return 'Giỏi'
					elif obj[12] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				else: return 'Giỏi'
			elif obj[18] == 'B':
				# {"feature": "M\u1ea1ng m\u00e1y t\u00ednh", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[20] == 'A':
					# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 3", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[22] == 'B':
						return 'Giỏi'
					elif obj[22] == 'C':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[20] == 'C':
					# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 6", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[26] == 'A':
						return 'Giỏi'
					elif obj[26] == 'B':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[20] == 'B':
					return 'Khá'
				elif obj[20] == 'D':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[18] == 'C':
				return 'Khá'
			else: return 'Giỏi'
		elif obj[16] == 'D':
			# {"feature": "L\u1eadp tr\u00ecnh tr\u1ef1c quan", "instances": 30, "metric_value": 1.4591, "depth": 3}
			if obj[19] == 'C':
				# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 12, "metric_value": 1.5546, "depth": 4}
				if obj[9] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[1] == 'D':
						return 'Trung bình'
					elif obj[1] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'B':
						return 'Trung bình'
					else: return 'Chưa Xếp Loại'
				elif obj[9] == 'C':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[19] == 'B':
				return 'Khá'
			elif obj[19] == 'A':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 4", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[23] == 'C':
					return 'Khá'
				elif obj[23] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[19] == 'D':
				# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 5, "metric_value": 1.371, "depth": 4}
				if obj[6] == 'D':
					# {"feature": "M\u1ea1ng m\u00e1y t\u00ednh", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[20] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[20] == 'C':
						return 'Trung bình'
					else: return 'Chưa Xếp Loại'
				elif obj[6] == 'B':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[19] == 'F':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		else: return 'Khá'
	elif obj[30] == 'C':
		# {"feature": "L\u1eadp tr\u00ecnh Web", "instances": 120, "metric_value": 1.7265, "depth": 2}
		if obj[25] == 'D':
			# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 2", "instances": 42, "metric_value": 1.3293, "depth": 3}
			if obj[18] == 'B':
				# {"feature": "An to\u00e0n v\u00e0 b\u1ea3o m\u1eadt th\u00f4ng tin", "instances": 23, "metric_value": 0.9656, "depth": 4}
				if obj[28] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'A':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[28] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5] == 'B':
						return 'Khá'
					elif obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[28] == 'D':
					# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[12] == 'B':
						return 'Khá'
					elif obj[12] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[12] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[28] == 'A':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0] == 'B':
						return 'Khá'
					elif obj[0] == 'A':
						return 'Khá'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[18] == 'C':
				# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[15] == 'B':
					return 'Khá'
				elif obj[15] == 'D':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[0] == 'B':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[15] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[18] == 'D':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 3", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[22] == 'D':
					# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[8] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[8] == 'D':
						return 'Trung bình'
					else: return 'Chưa Xếp Loại'
				elif obj[22] == 'B':
					return 'Trung bình'
				else: return 'Chưa Xếp Loại'
			elif obj[18] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2] == 'C':
					return 'Khá'
				elif obj[2] == 'B':
					return 'Trung bình'
				else: return 'Khá'
			else: return 'Khá'
		elif obj[25] == 'C':
			# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 30, "metric_value": 1.1989, "depth": 3}
			if obj[1] == 'D':
				# {"feature": "X\u00e1c su\u1ea5t th\u1ed1ng k\u00ea", "instances": 11, "metric_value": 1.4949, "depth": 4}
				if obj[13] == 'C':
					# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf h\u1ec7 th\u1ed1ng", "instances": 8, "metric_value": 1.4056, "depth": 5}
					if obj[21] == 'C':
						return 'Khá'
					elif obj[21] == 'A':
						return 'Khá'
					elif obj[21] == 'D':
						return 'Trung bình'
					elif obj[21] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[13] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[13] == 'D':
					return 'Trung bình'
				else: return 'Chưa Xếp Loại'
			elif obj[1] == 'C':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[17] == 'B':
					return 'Khá'
				elif obj[17] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[0] == 'B':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[17] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[1] == 'B':
				return 'Khá'
			elif obj[1] == 'A':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'B':
					return 'Khá'
				elif obj[0] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			else: return 'Khá'
		elif obj[25] == 'B':
			# {"feature": "Ki\u1ebfn tr\u00fac v\u00e0 t\u1ed5 ch\u1ee9c m\u00e1y t\u00ednh", "instances": 27, "metric_value": 1.7059, "depth": 3}
			if obj[11] == 'C':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf h\u1ec7 th\u1ed1ng", "instances": 14, "metric_value": 1.2871, "depth": 4}
				if obj[21] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[0] == 'C':
						return 'Khá'
					elif obj[0] == 'B':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[21] == 'B':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 5, "metric_value": 1.371, "depth": 5}
					if obj[0] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[0] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[11] == 'D':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 6, "metric_value": 1.2516, "depth": 4}
				if obj[17] == 'B':
					# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[15] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[15] == 'C':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[17] == 'D':
					return 'Trung bình'
				else: return 'Chưa Xếp Loại'
			elif obj[11] == 'B':
				# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8] == 'B':
					return 'Giỏi'
				elif obj[8] == 'C':
					return 'Khá'
				elif obj[8] == 'D':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[11] == 'A':
				return 'Giỏi'
			else: return 'Khá'
		elif obj[25] == 'A':
			# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 16, "metric_value": 1.4238, "depth": 3}
			if obj[6] == 'A':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 10, "metric_value": 0.9219, "depth": 4}
				if obj[4] == 'A':
					return 'Giỏi'
				elif obj[4] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'B':
						return 'Giỏi'
					elif obj[1] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[4] == 'C':
					return 'Xuất sắc'
				else: return 'Giỏi'
			elif obj[6] == 'C':
				# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[12] == 'A':
					return 'Giỏi'
				elif obj[12] == 'D':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[6] == 'B':
				return 'Khá'
			elif obj[6] == 'D':
				return 'Khá'
			else: return 'Giỏi'
		elif obj[25] == '0':
			return 'Chưa Xếp Loại'
		elif obj[25] == 'F':
			return 'Chưa Xếp Loại'
		else: return 'Khá'
	elif obj[30] == '0':
		return 'Chưa Xếp Loại'
	elif obj[30] == 'A':
		# {"feature": "L\u1eadp tr\u00ecnh Web", "instances": 101, "metric_value": 1.8522, "depth": 2}
		if obj[25] == 'A':
			# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 7", "instances": 28, "metric_value": 1.1393, "depth": 3}
			if obj[27] == 'A':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[17] == 'A':
					# {"feature": "C\u00f4ng ngh\u1ec7 Java", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[15] == 'A':
						return 'Xuất sắc'
					elif obj[15] == 'B':
						return 'Giỏi'
					else: return 'Xuất sắc'
				elif obj[17] == 'B':
					return 'Giỏi'
				elif obj[17] == 'C':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[27] == 'B':
				return 'Giỏi'
			elif obj[27] == 'C':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'A':
					return 'Xuất sắc'
				elif obj[0] == 'B':
					return 'Khá'
				else: return 'Xuất sắc'
			else: return 'Giỏi'
		elif obj[25] == 'C':
			# {"feature": "C\u01a1 s\u1edf d\u1eef li\u1ec7u", "instances": 27, "metric_value": 1.5012, "depth": 3}
			if obj[16] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 11, "metric_value": 1.5395, "depth": 4}
				if obj[2] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 5, "metric_value": 1.371, "depth": 5}
					if obj[1] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				elif obj[2] == 'A':
					return 'Giỏi'
				elif obj[2] == 'C':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[16] == 'C':
				# {"feature": "L\u1eadp tr\u00ecnh tr\u1ef1c quan", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[19] == 'B':
					return 'Khá'
				elif obj[19] == 'A':
					return 'Khá'
				elif obj[19] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'C':
						return 'Khá'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[16] == 'A':
				# {"feature": "To\u00e1n r\u1eddi r\u1ea1c", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[9] == 'B':
					return 'Giỏi'
				elif obj[9] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'B':
						return 'Giỏi'
					elif obj[1] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				else: return 'Giỏi'
			elif obj[16] == 'D':
				return 'Khá'
			else: return 'Khá'
		elif obj[25] == 'D':
			# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 4", "instances": 22, "metric_value": 1.2433, "depth": 3}
			if obj[23] == 'A':
				# {"feature": "Ph\u00e2n t\u00edch thi\u1ebft k\u1ebf thu\u1eadt to\u00e1n", "instances": 18, "metric_value": 0.8031, "depth": 4}
				if obj[17] == 'B':
					return 'Khá'
				elif obj[17] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'D':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Giỏi'
					elif obj[1] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[17] == 'C':
					return 'Trung bình'
				else: return 'Khá'
			elif obj[23] == 'B':
				# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[1] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[0] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[1] == 'A':
					return 'Giỏi'
				else: return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[25] == 'B':
			# {"feature": "C\u01a1 s\u1edf d\u1eef li\u1ec7u", "instances": 20, "metric_value": 1.4406, "depth": 3}
			if obj[16] == 'B':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 5", "instances": 9, "metric_value": 0.9864, "depth": 4}
				if obj[24] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[24] == 'C':
					return 'Giỏi'
				elif obj[24] == 'A':
					return 'Khá'
				else: return 'Khá'
			elif obj[16] == 'A':
				return 'Giỏi'
			elif obj[16] == 'C':
				# {"feature": "M\u00f4n t\u1ef1 ch\u1ecdn 5", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[24] == 'A':
					# {"feature": "Thi\u1ebft k\u1ebf Web", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8] == 'C':
						return 'Khá'
					elif obj[8] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[24] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			else: return 'Khá'
		elif obj[25] == '0':
			return 'Chưa Xếp Loại'
		else: return 'Khá'
	elif obj[30] == 'D':
		# {"feature": "L\u1eadp tr\u00ecnh h\u01b0\u1edbng \u0111\u1ed1i t\u01b0\u1ee3ng", "instances": 14, "metric_value": 1.2638, "depth": 2}
		if obj[12] == 'C':
			return 'Khá'
		elif obj[12] == 'A':
			# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2] == 'B':
				return 'Chưa Xếp Loại'
			elif obj[2] == 'C':
				return 'Khá'
			else: return 'Chưa Xếp Loại'
		elif obj[12] == 'B':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[0] == 'B':
				return 'Chưa Xếp Loại'
			elif obj[0] == 'C':
				return 'Khá'
			elif obj[0] == 'D':
				return 'Trung bình'
			else: return 'Chưa Xếp Loại'
		elif obj[12] == 'D':
			return 'Chưa Xếp Loại'
		else: return 'Khá'
	elif obj[30] == 'F':
		return 'Chưa Xếp Loại'
	else: return 'Khá'
